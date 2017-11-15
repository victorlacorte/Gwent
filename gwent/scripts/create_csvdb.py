import requests
from gwent.apiclient import factions_url, rarities_url, cardfactions_url, \
        cardrarities_url, categorize, merge_collections
from gwent.csvhelpers import write_csv


if __name__ == '__main__':
    r1 = requests.get(factions_url)
    r2 = requests.get(rarities_url)
    cards1 = categorize(r1.json(), cardfactions_url)
    cards2 = categorize(r2.json(), cardrarities_url)
    cards = merge_collections(cards1, cards2)
    write_csv(cards, ['Name', 'Faction', 'Rarity'], 'gwent/data/allcards.csv')
