import csv


def read_csv_file(csv_file_name):
    rows = []
    with open(csv_file_name, encoding='utf-8', mode='r') as csv_file:
        if csv_file is None:
            print(f'read_csv_file: Failed to open csv file {csv_file_name}.')
            return rows

        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)

    return rows


def write_csv_file(csv_file_name, rows):
    # rows is a list of dict
    if len(rows) == 0:
        print('write_csv_file: No rows to write.')
        return False

    header = list(rows[0].keys())

    with open(csv_file_name, encoding='utf-8', mode='w') as csv_file:
        if csv_file is None:
            print(f'write_csv_file: Failed to open csv file {csv_file_name}.')
            return False

        writer = csv.DictWriter(csv_file, fieldnames=list(rows[0].keys()), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

    return True

