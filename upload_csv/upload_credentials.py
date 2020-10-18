import os
import datetime
from csv_util import read_csv_file
from cloud_storage_util import set_credentials_json, upload_blob


def get_env_var(env_var_name):
    env_var = ''
    if env_var_name in os.environ:
        env_var = os.environ[env_var_name]
    else:
        print(f'get_env_var: Failed to get {env_var_name}.')
    return env_var


def get_env_vars():
    global credentials_json_path
    global csv_bucket_name

    credentials_json_path = get_env_var('SERVICE_ACCOUNT_CREDENTIALS_JSON')
    if credentials_json_path == '':
        return False

    csv_bucket_name = get_env_var('NEWGARDEN_SERVICE_ACCOUNT_DATA_BUCKET')
    if csv_bucket_name == '':
        return False

    # success
    return True


def main():
    print('\nStarting upload_credentials.py ...')

    success = get_env_vars()
    if not success:
        print('get_env_vars failed.  Exit.')
        return

    print('Env vars:')
    print(f'credentials_json_path: {credentials_json_path}')
    print(f'csv_bucket_name: {csv_bucket_name}')

    set_credentials_json(credentials_json_path)
    destination_blob_name = credentials_json_path
    success = upload_blob(csv_bucket_name, credentials_json_path, destination_blob_name)
    if not success:
        print('upload_blob failed.  Exit.')
        return


if __name__ == '__main__':
    main()

