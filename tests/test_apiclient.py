import json
import pytest
import requests
from gwent.apiclient import req_pagecards, filter_pagecards, get_cardlinks, \
        rarities_url, categorize, cards_url

@pytest.mark.ignore
def test_get_cardnames():
    cards = req_pagecards()
    assert cards.ok
    fcards = filter_pagecards(cards)
    assert fcards['count'] > 0
    assert 'last-modified' in fcards.keys()
    assert 'cards' in fcards.keys()

@pytest.mark.ignore
def test_get_cardlinks():
    with open('gwent/data/cardlinks.json', 'r') as f:
        jsonf = json.load(f)
        assert len(list(get_cardlinks(jsonf))) == jsonf['count']

def test_categorize():
    r = requests.get(rarities_url)
    rarities = '{}/{}'.format(cards_url, 'rarities')
    assert len(categorize(r.json(), rarities)) == 357
