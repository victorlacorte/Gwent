from gwent.jsonhelpers import write_json
from gwent.jsonhandler import process_json

if __name__ == '__main__':
    write_json(process_json('gwent/data/cards.json'),
               '/mnt/stuff/Users/vlacorte/Documents/Gwent/cards_enUS.json')
