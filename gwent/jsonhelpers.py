import json
# TODO possible circular dependency?
#from gwent.apiclient import api_url


cardsdb = 'gwent/data/cardsdb.json'

# TODO creathe a scheme such that we only alter the 'master' cards file
#   when the 'last-modified' header changes.

def write_json(data_json, fname):
    with open(fname, 'w') as f:
        json.dump(data_json, f, sort_keys=True, indent=4, ensure_ascii=False)

def get_lastmodified(fname=cardsdb):
    # Open the file
    with open(fname, 'r') as f:
        jsonf = json.load(f)
        return jsonf['last-modified']
