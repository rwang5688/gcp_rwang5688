import json


def write_json_file(json_file_name, rows):
    with open(json_file_name, encoding='utf-8', mode='w') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=4)

