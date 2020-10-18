from cloud_storage_util import download_blob
import json
from google.oauth2 import service_account


NEWGARDEN_SERVICE_ACCOUNT_DATA_BUCKET = 'newgarden-service-account-data-bucket'
SERVICE_ACCOUNT_CREDENTIALS_JSON = 'newgarden-cloud-functions-9f405fe88d29.json'


def download_credentials():
    bucket_name = NEWGARDEN_SERVICE_ACCOUNT_DATA_BUCKET
    source_blob_name = SERVICE_ACCOUNT_CREDENTIALS_JSON
    tmp_file_name = '/tmp/' + SERVICE_ACCOUNT_CREDENTIALS_JSON
    success = download_blob(bucket_name, source_blob_name, tmp_file_name)
    return success


def get_credentials():
    success = download_credentials()
    if not success:
        print('get_credentials: Failed to download_credentials.')
        return None

    credentials = None
    tmp_file_name = '/tmp/' + SERVICE_ACCOUNT_CREDENTIALS_JSON
    with open(tmp_file_name) as credentials_json_file:
        info = json.load(credentials_json_file)
        credentials = service_account.Credentials.from_service_account_info(info)
    return credentials

