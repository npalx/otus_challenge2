import csv
import json

from datetime import datetime

FILE_NAME_DATE_FORMAT = '%d-%m-%y %H:%M:%S'


def print_to_stdout(_, data):
    print(data)


def get_file_name(part_of_speech: str, code_element: str, extention: str):
    date = datetime.now().strftime(FILE_NAME_DATE_FORMAT)
    file_name = f'{code_element} {part_of_speech} {date}.{extention}'
    return file_name


def save_to_csv(parameters, data):
    file_name = get_file_name(parameters.part_of_speech, parameters.code_element, 'csv')

    with open(file_name, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for word_count_list in data:
            csv_writer.writerow(word_count_list)


def save_to_json(parameters, data):
    result = {
        'repository_url': parameters.url_path,
        'part_of_speech': parameters.part_of_speech,
        'code_element': parameters.code_element,
        'data': dict(data),
    }

    dump = json.dumps(result, ensure_ascii=False)

    file_name = get_file_name(parameters.part_of_speech, parameters.code_element, 'json')
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json_file.write(dump)
