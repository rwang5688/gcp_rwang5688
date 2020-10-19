from googleapiclient.discovery import build


def get_sheets(credentials):
    sheets_api = build('sheets', 'v4', credentials=credentials)
    sheets = sheets_api.spreadsheets()
    return sheets


def get_header(sheets, spreadsheet_id, header_range_name):
    result = sheets.values().get(spreadsheetId=spreadsheet_id,
                                    range=header_range_name).execute()
    header = result.get('values', [])
    return header

