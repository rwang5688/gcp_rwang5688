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


    def get_worksheet_rows(self):
        return self.worksheet.rows


    def get_worksheet_columns(self):
        return self.worksheet.cols


    def get_worksheet_headers(self):
        worksheet_headers = self.worksheet.get_row(1, include_tailing_empty=False)
        return worksheet_headers


    def add_worksheet_rows(self, rows):
        self.worksheet.add_rows(rows)

