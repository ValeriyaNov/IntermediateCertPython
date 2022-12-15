#import controller
import import_data


# Создаем новый контакт, сохраняем в loger.txt
def new_contact():
    first_name = input_firstname()
    last_name = input_lastname()
    patronymic = input_patronymic()
    date_of_birth = input('Дата рождения: ')
    phone_number = input('Номер телефона: ')
    mail = input('Эл. почта: ')
    contact_details = ('[' + first_name + ' ' + last_name + ' ' + patronymic +
                       '; ' + date_of_birth + '; ' + phone_number + '; ' + mail + ']')
    write_to_file('loger.txt', contact_details)
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


# Вводим отчество
def input_patronymic():
    first = input('Отчество: ')
    pa_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + pa_name


# Открываем и записываем в файл
def write_to_file(file_name, result):
    with open(file_name, 'a+', encoding='utf-8') as f_obj:
        f_obj.write(result + '\n')


# Открываем и читаем файл
def read_file(file):
    with open(file,'r', encoding="utf8") as data:
        file_read = str(data.read())
    return file_read


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

