import json


def read_json_file(json_file_name):
    rows = []
    with open(json_file_name, encoding='utf-8', mode='r') as json_file:
        if json_file is None:
            print(f'read_json_file: Failed to open json file {json_file_name}.')
            return rows

        rows = json.load(json_file)

    return rows


def write_json_file(json_file_name, data_rows):
    # data_rows is a list of dict
    if len(data_rows) == 0:
        print('write_csv_file: No data rows to write.')
        return False

    with open(json_file_name, encoding='utf-8', mode='w') as json_file:
        if json_file is None:
            print(f'write_json_file: Failed to open json file {json_file_name}.')
            return False

        json.dump(data_rows, json_file, ensure_ascii=False, indent=4)

    return True

