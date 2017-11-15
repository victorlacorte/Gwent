import csv


def write_csv(data_dict, header_vals, fname):
    '''
        Given a data_dict with card names (str) as keys and a list of
           attributes as values, create a CSV file with header_vals (list) as
           the header and data_dict items as row values.
    '''
    with open(fname, 'w') as f:
        dwriter = csv.writer(f)
        dwriter.writerow(header_vals)
        for k, v in data_dict.items():
            dwriter.writerow([k] + v)
