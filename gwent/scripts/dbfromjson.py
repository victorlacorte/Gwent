import json
from gwent.csvhelpers import json2csv

if __name__ == '__main__':
    fieldnames = ['name', 'type', 'rarity', 'faction', 'ingameId', 'info',
                  'flavor']
    fname = '/mnt/stuff/Users/vlacorte/Documents/Gwent/cards_enUS.csv'
    with open('gwent/data/cards_enUS.json', 'r') as f:
        jcards = json.load(f)
        json2csv(fname, jcards, fieldnames)
