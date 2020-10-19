from cloud_storage_util import set_credentials_json, download_blob
from csv_util import read_csv_file


def get_tmp_file_name(blob_name):
    file_name = blob_name.split('/')[-1]
    tmp_file_name = '/tmp/' + file_name
    return tmp_file_name


def download_blob_based_on_event(event):
    bucket_name = event['bucket']
    source_blob_name = event['name']
    tmp_file_name = get_tmp_file_name(source_blob_name)
    set_credentials_json('')
    success = download_blob(bucket_name, source_blob_name, tmp_file_name)
    return success


def read_csv_file_based_on_event(event):
    success = download_blob_based_on_event(event)
    if not success:
        print('read_csv_file_based_on_event: Failed to download_blob_based_on_event.')
        print(f'event: {event}')
        return None

    source_blob_name = event['name']
    tmp_file_name = get_tmp_file_name(source_blob_name)
    return read_csv_file(tmp_file_name)

