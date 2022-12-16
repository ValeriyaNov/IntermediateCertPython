import csv
import json
from menu import path_csv_data
from menu import path_json_data


def export_json(file_path):
    with open(path_json_data, 'r', encoding='UTF-8') as file: 
        data = json.load(file)
    with open("{file_path}.json", "W", encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write(',\n')
        print(f'Данные успешно сохранены в файл {file_path}.json')