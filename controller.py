import operations
import export_data
import import_data
import csv
import searchcontact
import datetime

def distribute(n):
    if n == '1':
        temp = operations.new_contact()
        #temp = operations.new_contact()
        enter = input('Нажмите Enter для завершения')


    elif n == '2':
        print('Выберите формат отображения данных: 1 - Построчно; 2 - В одну строку', sep = '\n')
        num = int(input())
        if num == 1 or num == 2:
            operations.read_contact(num)
            #operations.read_contact(num)
        enter = input('Нажмите Enter для выхода в меню ')


    elif n == '3':
        
        file_name_expott = input('Нипишите имя файла куда вы хотите скопировать данные: ')
        print('Выберите формат экспорта данных:', '1 - xml', '2 - json', '3 - csv', sep='\n')
        num_exp = input()
        if num_exp == '1':
            export_data.csv_to_json(file_name_expott)
            print(f'Данные успешно сохранены в файл {file_name_expott}.json\n')
        elif num_exp == '2':
            export_data.csv_to_csv(file_name_expott)
            print(f'Данные успешно сохранены в файл {file_name_expott}.csv\n')


    elif n == '4':
        id_note = input('Напишите id заметки')
        operations.redact_notes(id_note)
        

    elif n == '5':
        print('Выберите формат поиска:', '1 - по id', '2 - по заголовку', '3 - по дате', sep='\n')
        num_exp = input()
    
        if num_exp == '1':
            id = input('Введите id')
            searchcontact.search_id(id)
            
        elif num_exp == '2':
            name = input('Введите заголовок')
            searchcontact.search_name(name)

        elif num_exp == '3':
            str = (input('Введите дату в формате год, месяц, день через запятую без пробелов')).split(",")
            year = (str[0])
            mon = (str[1])
            day = (str[2])
            date = f"{year}-{mon}-{day}"
            searchcontact.search_date(date)
        
        enter = input('Нажмите Enter для завершения')

    elif n == '6':
        id_note = input('Напишите id заметки')
        operations.dell_notes(id_note)
