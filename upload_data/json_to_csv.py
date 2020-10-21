from json_util import read_json_file
from csv_util import write_csv_file


def parse_arguments():
    import argparse
    global json_file_name

    parser = argparse.ArgumentParser()
    parser.add_argument('json_file_name', help='json file name.')

    args = parser.parse_args()
    json_file_name = args.json_file_name

    if json_file_name is None:
        print('parse_arguments: json_file_name is missing.')
        return False

    # success
    return True


def main():
    print('\nStarting json_to_csv.py ...')

    success = parse_arguments()
    if not success:
        print('parse_arguments failed.  Exit.')
        return

    print('Args:')
    print(f'json_file_name: {json_file_name}')

    json_rows = read_json_file(json_file_name)
    print('JSON rows:')
    print(json_rows)

    file_name_base = json_file_name.split('.')[0]
    print(f'file_name_base: {file_name_base}')

    csv_file_name = file_name_base + '.csv'
    print(f'csv_file_name: {csv_file_name}')

    success = write_csv_file(csv_file_name, json_rows)
    if not success:
        print('write_csv_file failed.  Exit.')
        return


if __name__ == '__main__':
    main()

