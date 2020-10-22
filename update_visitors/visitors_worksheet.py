from env_var import get_env_var
from credentials_util import get_credentials
import pygsheets


class VisitorsWorksheet:
    def __init__(self):
        success = self.set_credentials()
        if not success:
            return

        self.client = pygsheets.authorize(custom_credentials=self.credentials)
        if self.client is None:
            return

        success = self.set_worksheet()
        if not success:
            return

        success = self.set_worksheet_headers()
        if not success:
            return

        print('VisitorsWorksheet.__init__: Connected to Visitors worksheet.')


    def set_credentials(self):
        self.credentials = get_credentials()
        if self.credentials is None:
            print('VisitorsWorksheet.set_credentials: Failed to get_credentials.')
            return False

        print(f'VisitorsSheet.set_credentials: self.credentials={self.credentials}.')
        return True


    def set_worksheet(self):
        spreadsheet_id = get_env_var('NEWGARDEN_VISITORS_SPREADSHEET_ID')
        if spreadsheet_id == '':
            return False

        self.sheet = self.client.open_by_key(spreadsheet_id)
        if self.sheet is None:
            print('VisitorsWorksheet.set_worksheet: Failed to open spreadsheet by key.')
            return False

        worksheet_title = get_env_var('NEWGARDEN_VISITORS_WORKSHEET_TITLE')
        if worksheet_title == '':
            return False

        self.worksheet = self.sheet.worksheet_by_title(worksheet_title)
        if self.worksheet is None:
            print('VisitorsWorksheet.set_worksheet: Failed to get worksheet by title.')
            return False

        return True


    def set_worksheet_headers(self):
        self.worksheet_headers = self.worksheet.get_row(1, include_tailing_empty=True)
        enumerated_headers = list(enumerate(self.worksheet_headers))
        enumerated_headers = [tuple_object for tuple_object in enumerated_headers if tuple_object[1]]
        pos_headers_lookup_table = dict(enumerated_headers)
        self.worksheet_headers_pos_lookup_table = {value: key for key, value in pos_headers_lookup_table.items()}

        return True


    def add_data_row(self, data_row):
        # data_row is a dict
        headers = self.worksheet_headers
        keys = data_row.keys()
        # debug
        print(f'VisitorsWorksheet.add_data_row: headers={headers}')
        print(f'VisitorsWorksheet.add_data_row: keys={keys}')

        values = []
        for header in headers:
            value = ''
            if header in keys:
                value = data_row[header]
                # debug
                print(f'VisitorsWorksheet.add_data_row: header={header}, value={value}')
            values.append(value)

        last_row = self.worksheet.rows
        self.worksheet.insert_rows(last_row, number=1, values=values, inherit=True)


    def update_data_rows(self, data_rows):
        # data_rows is a list of dict
        rows_before = self.worksheet.rows
        for data_row in data_rows:
            self.add_data_row(data_row)
        rows_after = self.worksheet.rows
        rows_added = rows_after - rows_before
        # debug
        print(f'VisitorsWorksheet.update_data_rows: added {rows_added} rows.')

