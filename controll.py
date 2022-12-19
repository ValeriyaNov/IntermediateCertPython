import operations
import export_data
import import_data
import searchh
import csv

def distrib(n):
    if n == '1':
        temp = operations.new_contact()
        enter = input('Нажмите Enter для завершения')

    elif n == '2':
        print('Выберите формат отображения данных: 1 - Построчно; 2 - В одну строку', sep = '\n')
        num = int(input())
        if num == 1 or num == 2:
            operations.read_contact(num)
        enter = input('Нажмите Enter для выхода в меню ')

    elif n == '3':
        '''
        если вы все данные из своего файла скопируете в файл, 
        который укажет пользователь, то это можно считать экспортом
        '''
        
        file_name_expott = input('Нипишите имя файла, куда вы хотите скопировать данные: ')
        num_exp = int(input('Выберите формат экспорта данных: 1 - xml, 2 - csv'))
        if num_exp == 1:
            export_data.export_to_xml(file_name_expott)
            print('Данные успешно экспортированы в формате xml!\n')
        elif num_exp == 2:
            path = 'phonebook.csv'
            def import_csv(path_to_import_csv_file): 
                data = []        
                with open(path_to_import_csv_file, "r", newline='', encoding='utf-8') as file:
                    
                    file_reader = csv.DictReader(file, delimiter = ",") 
                    for row in file_reader:
                        g = list(row.values())
                        d = g[0].split(';')
                        print(d, type(d))
                        data.append(g)     
                return data

            arr1 = import_csv(path)
            print(arr1)
            for i in range(0, len(arr1)):
                k = arr1[i]
                #print(k)
                for i in range(len(k)):
                    j = k[i]
                    print(type(j))
                    with open(file_name_expott, "a", encoding='utf-8') as fil:
                        csv_fil = csv.writer(fil, delimiter=',')
                        csv_fil.writerow(j.split(';'))
            print('Данные успешно записаны')


            # r_file = open('phonebook.csv',encoding='utf-8')
            # file_reader = csv.reader(r_file, delimiter = ";")
            # print(file_reader)
            # with open(file_name_expott, "a", encoding='utf-8') as file:
            #     file_writer = csv.writer(file, delimiter = ";", lineterminator="\r")
            #     for row in file_reader:
            #         file_writer.writerow(file_reader)
            print('Данные успешно сохранены в файл')
        else:
            print('Пожалуста, введите номер пункта меню: ')
        
     
        #       #export_data.export_json(file_name_expott)
        #     export_data.convjson(file_name_expott)
        #     print('Данные успешно экспортированы в формате json!\n')
        # 
        #     enter = input('Нажмите Enter для выхода в меню ')

        enter = input('Нажмите Enter для завершения')

    elif n == '4':
        '''
        считывание и сохранение, в вашу базу, записей из файла, 
        который указал пользователь
        '''
        

        num = int(input('Выберете тип файла, из которого будете брать данные 1 - csv, 2 - json   '))
        if num == 1:
            arr1 = import_data.copy_cont()    
            for i in range(len(arr1)):
                with open('phonebook.csv', "a", encoding='utf-8') as fil:
                    csv_fil = csv.writer(fil, delimiter=';')
                    csv_fil.writerow(arr1[i])
                    print('Данные успешно записаны')
        if num == 2:
            import_data.copy_cont_json()
        enter = input('Нажмите Enter для завершения')


    elif n == '5':
        user_search = input('Введите имя для поиска?: ')
        searchh.searchcontact(user_search)
        enter = input('Нажмите Enter для завершения')