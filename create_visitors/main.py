from cloud_storage_util import set_credentials_json, download_blob
from csv_util import read_csv_file
from credentials_util import get_credentials
from google_sheets_util import get_sheets, get_header


VISITORS_SPREADSHEET_ID = '1NX2DQrM2WlVpZdUQHqoSy9jFQHiI-JlWtxCPaMVPKpk'
VISITORS_HEADER_RANGE_NAME = 'Visitors!A1:AI1'


def preamble(event, context):
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('Blob: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))


def get_tmp_file_name(blob_name):
    file_name = blob_name.split('/')[-1]
    print(f'file_name: {file_name}')
    tmp_file_name = '/tmp/' + file_name
    print(f'tmp_file_name: {tmp_file_name}')
    return tmp_file_name


def download_blob_based_on_event(event):
    bucket_name = event['bucket']
    source_blob_name = event['name']
    tmp_file_name = get_tmp_file_name(source_blob_name)
    set_credentials_json('')
    success = download_blob(bucket_name, source_blob_name, tmp_file_name)
    return success


def read_csv_file_based_on_event(event):
    source_blob_name = event['name']
    tmp_file_name = get_tmp_file_name(source_blob_name)
    return read_csv_file(tmp_file_name)


def get_credentials_and_sheets():
    credentials = get_credentials()
    if credentials is None:
        print('get_visitor_header: Failed to get_credentials.')
        return None

    # debug
    print(f'get_visitors_header: credentials={credentials}.')

    sheets = get_sheets(credentials)
    if sheets is None:
        print('get_visitors_header: Failed to get_sheets.')
        return None

    return sheets


def get_visitors_header(sheets):
    visitors_header = get_header(sheets, VISITORS_SPREADSHEET_ID, VISITORS_HEADER_RANGE_NAME)
    return visitors_header


def create_visitors(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.
    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """
    preamble(event, context)

    success = download_blob_based_on_event(event)
    if not success:
        print('create_visitors: Failed to download_blob_based_on_event.')
        print(f'event: {event}')
        print('Exit.')
        return

    rows = read_csv_file_based_on_event(event)
    if rows is None:
        print('create_visitors: Failed to read_csv_file_based_on_event.')
        print(f'event: {event}')
        print('Exit.')
        return

    # debug
    print('create_visitors: CSV file rows:')
    print(rows)

    sheets = get_credentials_and_sheets()
    if sheets is None:
        print('create_visitors: Failed to get_credentials_and_sheets.')
        print('Exit.')
        return

    visitors_header = get_visitors_header(sheets)
    if visitors_header is None:
        print('creaete_visitors: Failed to get_visitors_header.')
        print('Exit.')
        return

    # debug
    print(f'create_visitors: visitors_header={visitors_header}.')

