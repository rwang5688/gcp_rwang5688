from env_var import get_env_var
from json_util import read_json_file
import datetime
from cloud_storage_util import set_credentials_json, upload_blob


def get_env_vars():
    global credentials_json_path
    global visitors_data_bucket_name

    credentials_json_path = get_env_var('SERVICE_ACCOUNT_CREDENTIALS_JSON')
    if credentials_json_path == '':
        return False

    visitors_data_bucket_name = get_env_var('NEWGARDEN_VISITORS_DATA_BUCKET')
    if visitors_data_bucket_name == '':
        return False

    # success
    return True


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
    print('\nStarting upload_visitors_json.py ...')

    success = get_env_vars()
    if not success:
        print('get_env_vars failed.  Exit.')
        return

    print('Env vars:')
    print(f'credentials_json_path: {credentials_json_path}')
    print(f'visitors_data_bucket_name: {visitors_data_bucket_name}')

    success = parse_arguments()
    if not success:
        print('parse_arguments failed.  Exit.')
        return

    print('Args:')
    print(f'json_file_name: {json_file_name}')

    # debug: read and print data rows
    data_rows = read_json_file(json_file_name)
    print('data_rows:')
    print(data_rows)

    today = datetime.date.today()
    destination_blob_name = str(today) + "/" + json_file_name
    print(f'destination_blob_name: {destination_blob_name}')

    set_credentials_json(credentials_json_path)
    success = upload_blob(visitors_data_bucket_name, json_file_name, destination_blob_name)
    if not success:
        print('upload_blob failed.  Exit.')
        return


if __name__ == '__main__':
    main()

