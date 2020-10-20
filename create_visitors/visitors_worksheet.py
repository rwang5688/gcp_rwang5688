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


    def get_worksheet_headers(self):
        worksheet_headers = self.worksheet.get_row(1, include_tailing_empty=False)
        return worksheet_headers


    def add_csv_row(self, csv_row):
        # note: each csv_row is a dict
        headers = self.get_worksheet_headers()
        keys = csv_row.keys()
        # debug
        print(f'VisitorsWorksheet.add_csv_row: headers={headers}')
        print(f'VisitorsWorksheet.add_csv_row: keys={keys}')

        values = []
        for header in headers:
            value = ''
            if header in keys:
                value = csv_row[header]
                # debug
                print(f'VisitorsWorksheet.add_csv_row: header={header}, value={value}')
            values.append(value)

        last_row = self.worksheet.rows
        self.worksheet.insert_rows(last_row, number=1, values=values, inherit=True)


    def add_csv_rows(self, csv_rows):
        rows_before = self.worksheet.rows
        for csv_row in csv_rows:
            self.add_csv_row(csv_row)
        rows_after = self.worksheet.rows
        rows_added = rows_after - rows_before
        # debug
        print(f'VisitorsWorksheet.add_csv_rows: added {rows_added} rows.')

