#import controller
import import_data
import json
import csv


# Создаем новый контакт, сохраняем в loger.txt
def new_contact():
    first_name = input_firstname()
    last_name = input_lastname()
    patronymic = input_patronymic()
    date_of_birth = input('Дата рождения: ')
    phone_number = input('Номер телефона: ')
    mail = input('Эл. почта: ')
    #contact_details = ('[Name' + first_name + ' last name ' + last_name + 
    #                   ' Patronymic: ' + patronymic +
    #                   '; Date of birth: ' + date_of_birth + '; Phone number' +
    #                   phone_number + '; Email' + mail + ']')
    contact_details = {'Имя': first_name, 'Фамилия': last_name, 
                       'Отчество': patronymic,
                       'Дата рождения': date_of_birth, 'Номер телефона':
                       phone_number, 'Email': mail}
    #write_to_file('loger.txt', contact_details)  Не использется т.к. нет в условии задачи
    #print('Данные успешно сохранены')
    return contact_details


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


# Вводим отчество
def input_patronymic():
    first = input('Отчество: ')
    pa_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + pa_name


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
'''     


def read_json():
    with open('import.json', 'r', encoding='UTF-8') as file: 
        data = json.load(file)
        print(data)
        
def read_csv():        
    with open('import.csv', "r", newline='', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter = ";") 
        for row in file_reader:
            print(row)


# Поиск
def searchcontact():
    searchname = input('Введите имя для поиска среди записей: ')
    se_name = searchname[1:]
    firstchar = searchname[0]
    searchname = firstchar.upper() + se_name
    myfile= open(filename, 'r+')
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if searchname in line:
            print('Результат поиска: ', end = ' ')
            print( line)
            found = True
            break
    if found == False:
        print('Запрашиваемый Вами контакт не найден', searchname) 



