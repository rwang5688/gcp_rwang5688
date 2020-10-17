import os
from csv_file import read_csv_file


def get_env_var(env_var_name):
    env_var = ''
    if env_var_name in os.environ:
        env_var = os.environ[env_var_name]
    else:
        print(f'get_env_var: Failed to get {env_var_name}.')
    return env_var


def get_env_vars():
    global csv_bucket_name

    csv_bucket_name = get_env_var('NEWGARDEN_VISITORS_CSV_DATA_BUCKET')
    if csv_bucket_name == '':
        return False

    # success
    return True


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
    print('\nStarting upload_visitors_csv.py ...')

    success = get_env_vars()
    if not success:
        print('get_env_vars failed.  Exit.')
        return

    print('Env vars:')
    print(f'csv_bucket_name: {csv_bucket_name}')

    success = parse_arguments()
    if not success:
        print('parse_arguments failed.  Exit.')
        return

    print('Args:')
    print(f'csv_file_name: {csv_file_name}')

    # debug: print CSV file rows
    rows = read_csv_file(csv_file_name)
    print('CSV file rows:')
    print(rows)


if __name__ == '__main__':
    main()

