from env_var import get_env_var
from cloud_storage_util import download_blob
import json
from google.oauth2 import service_account


def download_credentials():
    bucket_name = get_env_var('SERVICE_ACCOUNT_DATA_BUCKET')
    if bucket_name == '':
        return None

    credentials_json_path = get_env_var('SERVICE_ACCOUNT_CREDENTIALS_JSON')
    if credentials_json_path == '':
        return None

    source_blob_name = credentials_json_path
    tmp_file_name = '/tmp/' + credentials_json_path
    success = download_blob(bucket_name, source_blob_name, tmp_file_name)

    return success


def get_credentials():
    success = download_credentials()
    if not success:
        print('get_credentials: Failed to download_credentials.')
        return None

    credentials_json_path = get_env_var('SERVICE_ACCOUNT_CREDENTIALS_JSON')
    if credentials_json_path == '':
        return None

    credentials = None
    tmp_file_name = '/tmp/' + credentials_json_path
    with open(tmp_file_name) as credentials_json_file:
        info = json.load(credentials_json_file)
        credentials = service_account.Credentials.from_service_account_info(info)

    return credentials

