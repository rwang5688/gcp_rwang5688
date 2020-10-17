import csv


def read_csv_file(csv_file_name):
    results = []
    with open(csv_file_name, encoding='utf-8', mode='r') as csv_file:
        if csv_file is None:
            print(f'read_csv_file: Failed to open csv file {csv_file_name}.')
            return results

        reader = csv.DictReader(csv_file)
        for row in reader:
            results.append(row)

    return results

