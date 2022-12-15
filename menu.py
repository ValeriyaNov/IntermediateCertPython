import controller


def select_work():
    
    #1. Добавление записи
    #2. Вывод записей на экран
    #3. Импорт
    #4. Экспорт
    
    
    return 0






filename = 'phonebook.txt'
myfile = open(filename, 'a+')
myfile.close


def greeting():
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')

def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')
        print('2. Вывод записей на экран')
        print('3. Импорт')
        print('4. Экспорт')
        print('5. Поиск')
        print('6. Выход\n') 
        controller.distribute(input('Выберите пункт меню: '))
        '''
        if n == '1':
            #new_contact()
            controller.new_contact()  # переходим в controller
            enter = input('Нажмите Enter для завершения')
            menu()
        elif n == '2':
            myfile = open(filename, 'r+')
            filecontents = myfile.read()
            if len(filecontents) == 0:
                print('Записей нет')
            else:
                print(filecontents)
            myfile.close
            enter = input('Нажмите Enter для завершения')
            menu()
        elif n == '5':
            searchcontact()
            enter = input('Нажмите Enter для завершения')
            menu()
        elif n == '6':
            print('Спасибо за просмотр')
        else:
            print('Пожалуста, введите номер пункта меню')
            enter = input('Нажмите Enter для завершения')
            menu()
            '''

            
            
'''
перенес в controller
def input_firstname():
    first = input('Имя: ')
    fi_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + fi_name

def input_lastname():
    first = input('Фамилия: ')
    la_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + la_name

def input_patronymic():
    first = input('Отчество: ')
    pa_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + pa_name

def new_contact():
    first_name = input_firstname()
    last_name = input_lastname()
    patronymic = input_patronymic()
    date_of_birth = input('Дата рождения: ')
    phone_number = input('Номер телефона: ')
    mail = input('Эл. почта: ')
    contact_details = ('[' + first_name + ' ' + last_name + ' ' + patronymic + '; ' + date_of_birth + '; ' + phone_number + '; ' + mail + ']')
    myfile = open(filename, 'a')
    myfile.write(contact_details)
    print('Данные успешно сохранены')
'''

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


greeting()
menu()