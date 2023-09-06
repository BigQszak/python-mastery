import csv

def read_csv_as_dicts(filename, convtypes = []):
    records = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            # Data conversion
            conv_row = [func(val) for func, val in zip(convtypes, row)]
        
            # Create single dict corresponding to a single row
            record = dict(zip(headers, conv_row))

            records.append(record)
    return records 