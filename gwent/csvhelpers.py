import csv


def write_csv(data_dict, header, fname):
    '''
        Given a data_dict with card names (str) as keys and a list of
           attributes as values, create a CSV file with a header (list)
           and data_dict items as row values.
    '''
    with open(fname, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for k, v in data_dict.items():
            # writerow expects a list as argument
            writer.writerow([k] + v)

def json2csv(fname, json_arr, fieldnames, restval='NA',
                 extrasaction='ignore', dialect='unix'):
    with open(fname, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval=restval,
                                extrasaction=extrasaction, dialect=dialect)

        writer.writeheader()
        for json_obj in json_arr:
            writer.writerow(json_obj)
