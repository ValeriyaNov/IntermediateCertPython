#import controller
import import_data
import json
import csv




# Создаем новый контакт, сохраняем в loger.txt
def new_contact():
    first_name = input_firstname()
    last_name = input_lastname()
    phone_number = input('Номер телефона: ')
    description = input_description()
    new_list = [first_name, last_name, phone_number, description]
    save_to_csv(new_list)
    #contact_details = {'Имя': first_name, 'Фамилия': last_name, 
    #                   'Отчество': patronymic,
    #                   'Дата рождения': date_of_birth, 'Номер телефона':
    #                   phone_number, 'Email': mail}
    print('Данные успешно сохранены')


# Вводим имя
def input_firstname():
    first = input('Имя: ')
    fi_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + fi_name


# Вводим фимилию
def input_lastname():
    first = input('Фамилия: ')
    la_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + la_name


def input_description():
    first = input('Описание: ')
    pa_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + pa_name


# Код от Александра
def save_to_csv(new_contacts):
    with open('phonebook.csv', 'a', encoding='utf-8') as bd:
        for i in range(len(new_contacts)):
            if i != len(new_contacts) - 1:
                bd.write(f'{new_contacts[i]};')
            else:
                bd.write(f'{new_contacts[i]}')
        bd.write('\n')


# Код от Александра
def read_contact(unit = 1, file_name = 'phonebook.csv'):
    with open(file_name, newline = '') as f:
        reader = csv.reader(f, delimiter='; ')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()


# Код Дениса
def read_csv():        
    with open('phonebook.csv', "r", newline='', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter = ";") 
        for row in file_reader:
            print(row)


''' Удалить в процессе т.к. не используется
# Открываем и записываем в файл
def write_to_file(file_name, result):
    with open(file_name, 'a+', encoding='utf-8') as f_obj:
        f_obj.write(result + '\n')

# Открываем и читаем файл
def read_file(file):
    with open(file,'r', encoding="utf8") as data:
        file_read = data.read()
    return file_read


def read_json():
    with open('import.json', 'r', encoding='UTF-8') as file: 
        data = json.load(file)
        print(data)
        
'''     

