from csv_util import read_csv_file
from json_util import write_json_file


def parse_arguments():
    import argparse
    global csv_file_name

    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file_name', help='csv file name.')

    args = parser.parse_args()
    csv_file_name = args.csv_file_name

    if csv_file_name is None:
        print('parse_arguments: csv_file_name is missing.')
        return False

    # success
    return True


def main():
    print('\nStarting csv_to_json.py ...')

    success = parse_arguments()
    if not success:
        print('parse_arguments failed.  Exit.')
        return

    print('Args:')
    print(f'csv_file_name: {csv_file_name}')

    csv_rows = read_csv_file(csv_file_name)
    print('CSV rows:')
    print(csv_rows)

    file_name_base = csv_file_name.split('.')[0]
    print(f'file_name_base: {file_name_base}')
    json_file_name = file_name_base + '.json'
    print(f'json_file_name: {json_file_name}')
    write_json_file(json_file_name, csv_rows)


if __name__ == '__main__':
    main()

