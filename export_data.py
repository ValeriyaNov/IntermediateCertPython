import csv
import json
#from menu import filename


# Копируем phonebook в указанный пользователем файл 
def csv_usrer(file_user, file_name = 'phonebook.csv'):
    with open('phonebook.csv', 'a') as bd:
        csv_f = csv.reader(bd, delimiter=';')
        print('врменно, удалить')
    with open(f'{file_user}.csv', 'a+') as file_user_bd:
        csv_f = csv.reader(file_user_bd, delimiter=';')
        print('file read')
        

def csv_to_data(file_name = 'phonebook.csv'):
    with open(file_name, newline='') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def export_to_xml(data = csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<contacts>\n'
    for row in data:
        first_name, last_name, phone_number, description = row
        xml += '    <contact>\n'
        xml += '        <Name>{}</Name>\n' \
            .format(first_name)
        xml += '        <Last_name>{}</Last_name>\n' \
            .format(last_name)
        xml += '        <Phone_number>{}</Phone_number>\n' \
            .format(phone_number)
        xml += '        <Info>{}</Info>\n' \
            .format(description)
        xml += '    </contact>\n'
    xml += '</contacts>'
    with open('phonebook.xml', 'w') as page:
        page.write(xml)
    return data



'''
def export_json(file_path):
    with open(path_json_data, 'r', encoding='UTF-8') as file: 
        data = json.load(file)
    with open("{file_path}.json", "W", encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write(',\n')
        print(f'Данные успешно сохранены в файл {file_path}.json')
'''
