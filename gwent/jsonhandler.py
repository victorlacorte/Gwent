import json
from collections import defaultdict

def get_csv(cards='gwent/data/cards.json'):
    csv = defaultdict(list)
    with open(cards, 'r') as f:
        jsoncards = json.load(f)
        for k, v in jsoncards.items():
            if v['released']:
                vk, vv = v['variations'].popitem()
                # TODO needs to be tested
                #if vv['availability'] != 'NonOwnable':
                if vv['collectible']:
                    name = v['name']['en-US']
                    faction = v['faction']
                    color = v['type']
                    csv[name].extend([color] + [faction])
    return csv


# This code is an abomination as it is right now. Let's try to further struct
#   it so that we get an intermediate JSON file with en-US info only.
# 'art', 'craft', 'mill' and 'variationId'  lie inside the 'variations' dict.
# Also worth noting that we consider only a *random* variation of a card
#   (by method dict.popitem).
ignored_keys = ['categories', 'infoRaw', 'ingameId', 'keywords', 'loyalties',
                'positions', 'related', 'art', 'craft', 'mill', 'variationId']
relevant_keys = ['name', 'faction', 'flavor', 'info', 'strength', 'type',
                 'availability', 'rarity', 'ingameId']

def process_json(cards, lang='en-US', relevant_keys=relevant_keys):
    pcards = []
    with open(cards, 'r') as f:
        jcards = json.load(f)
        for _, v in jcards.items():
            if v['released']:
                _, var_dict = v['variations'].popitem()
                if var_dict['collectible']:
                    tmp = {}
                    for k in relevant_keys:
                        if k in v:
                            if type(v[k]) is dict:
                                tmp.update({k: v[k][lang]})
                            else:
                                tmp.update({k: v[k]})
                        elif k in var_dict:
                            tmp.update({k: var_dict[k]})
                    pcards.append(tmp)
    return pcards
