from event_to_csv import read_csv_file_based_on_event
from visitors_worksheet import VisitorsWorksheet


def preamble(event, context):
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('Blob: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))


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

    csv_rows = read_csv_file_based_on_event(event)
    if csv_rows is None:
        print('create_visitors: Failed to read_csv_file_based_on_event.')
        print(f'event: {event}')
        print('Exit.')
        return

    # debug
    print('create_visitors: csv_rows:')
    print(csv_rows)

    visitors_worksheet = VisitorsWorksheet()
    if visitors_worksheet is None:
        print('create_visitors: Failed to initialize VisitorsWorksheet.')
        print('Exit.')
        return

    # debug
    print(f'create_visitors: visitors_worksheet:')
    print(visitors_worksheet)
    visitors_worksheet_rows = visitors_worksheet.get_worksheet_rows()
    visitors_worksheet_columns = visitors_worksheet.get_worksheet_columns()
    print(f'create_visitors: visitors_worksheet_rows={visitors_worksheet_rows}.')
    print(f'create_visitors: visitors_worksheet_columns={visitors_worksheet_columns}.')

    visitors_worksheet_headers = visitors_worksheet.get_worksheet_headers()
    if visitors_worksheet_headers is None:
        print('create_visitors: Failed to VisitorsWorksheet.get_worksheet_headers.')
        print('Exit.')
        return

    # debug
    print(f'create_visitors: visitors_worksheet_headers={visitors_worksheet_headers}.')

