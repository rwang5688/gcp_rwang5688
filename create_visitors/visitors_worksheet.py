from env_var import get_env_var
from credentials_util import get_credentials
from google_sheets_util import get_sheets, get_header


class VisitorsWorksheet:
    def __init__(self):
        self.credentials = None
        self.sheets = None
        success = self.set_credentials()
        if not success:
            print('VisitorsWorksheet.__init__: Failed to set_credentials.')
            return

        print(f'VisitorsSheet.__init__: self.credentials={self.credentials}.')

        success = self.set_sheets()
        if not success:
            print('VisitorsWorksheet.__init__: Failed to set_sheets.')
            return



    def set_credentials(self):
        self.credentials = get_credentials()
        if self.credentials is None:
            print('VisitorsWorksheet.set_credentials: Failed to get_credentials.')
            return False

        return True


    def set_sheets(self):
        self.sheets = get_sheets(self.credentials)
        if self.sheets is None:
            print('VisitorsWorksheet.set_sheets: Failed to get_sheets.')
            return False

        return True


    def get_header(self):
        spreadsheet_id = get_env_var('NEWGARDEN_VISITORS_SPREADSHEET_ID')
        if spreadsheet_id == '':
            return None

        header_range_name = get_env_var('NEWGARDEN_VISITORS_HEADER_RANGE_NAME')
        if header_range_name == '':
            return None

        header = get_header(self.sheets, spreadsheet_id, header_range_name)
        return header

