import asyncio
import csv
import json
import requests
from aiohttp import ClientSession
from collections import defaultdict


index_url = 'https://api.gwentapi.com/v0'
cards_url = '{}/{}'.format(index_url, 'cards')
factions_url = '{}/{}'.format(index_url, 'factions')
rarities_url = '{}/{}'.format(index_url, 'rarities')
cardfactions_url = '{}/{}'.format(cards_url, 'factions')
cardrarities_url = '{}/{}'.format(cards_url, 'rarities')

pagecard_params = {'limit': 500, 'offset': 0}

def req_pagecards(url, params=pagecard_params):
    return requests.get(url, params=params)

def filter_pagecards(cards_response):
    '''
        Obsolete function. Caching the API has no current usages.
    '''
    cards_json = cards_response.json()
    cards_json['cards'] = cards_json.pop('results')  # rename the key
    cards_json['last-modified'] = cards_response.headers['last-modified']
    return cards_json

# http://mahugh.com/2017/05/23/http-requests-asyncio-aiohttp-vs-requests/
def fetch_async(urls):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(fetch_all(urls))
    loop.run_until_complete(future)
    return future.result()

async def fetch_all(urls):
    tasks = []
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)
        return await asyncio.gather(*tasks)

async def fetch(url, session):
    async with session.get(url) as response:
        resp = await response.json()
        return resp

def categorize(collection_json, category_url, params=pagecard_params):
    '''
        Return a dict with card names as keys and their respective collection
            attributes as values.


        collection_json: the JSON API response of a given collection (i.e.
            /factions or /rarities);

        category_url: the /cards/[factions, rarities] URL to be requested;

        params: dict with (mainly) 'limit' and 'offset' keys.
    '''
    all_cards = {}
    # Each category is a dict with 'name', 'href' and 'uuid' keys.
    for category in collection_json:
        cat_name = category['name']
        # URL to request all cards given a specific attribute. Since a category
        #   has attributes for all cards in the game, querying each one
        #   individually gathers all possible cards.
        url = '{}/{}'.format(category_url, category['uuid'])
        cards = req_pagecards(url, params).json()['results']
        for card in cards:
            all_cards[card['name']] = cat_name
    return all_cards

def merge_collections(collection1, *collections):
    '''
        Return a dict with each collection's attributes of all cards.


        collection: dict with card names as keys and a collection's attribute
            as value.
    '''
    d = defaultdict(list)
    for k, v in collection1.items():
        d[k].append(v)
    for collection in collections:
        for k, v in collection.items():
            d[k].append(v)
    return d
