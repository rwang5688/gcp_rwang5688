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

    rows = read_csv_file_based_on_event(event)
    if rows is None:
        print('create_visitors: Failed to read_csv_file_based_on_event.')
        print(f'event: {event}')
        print('Exit.')
        return

    # debug
    print('create_visitors: CSV file rows:')
    print(rows)

    visitors_wks = VisitorsWorksheet()
    visitors_header = visitors_wks.get_header()
    if visitors_header is None:
        print('creaete_visitors: Failed to VisitorsWorksheet.get_header.')
        print('Exit.')
        return

    # debug
    print(f'create_visitors: visitors_header={visitors_header}.')

