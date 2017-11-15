import json


def write_json(jsondata, fname):
    with open(fname, 'w') as f:
        json.dump(jsondata, f, sort_keys=True, indent=4, ensure_ascii=False)
