import operations
import export_data
import import_data
import searchcontact


def distribute(n):
    if n == '1':
        temp = operations.new_contact()  # переходим в operations
        enter = input('Нажмите Enter для завершения')

    elif n == '2':
        operations.read_csv(n)   # первый метод должен просто вывести в консоль

        # второй метод с выбором как вывести
        #print('Выберите формат отображения данных: 1 - Построчно; 2 - В одну строку', sep = '\n')
        #num = int(input())
        #if num == 1 or num == 2:
        #    operations.read_contact(num)
        enter = input('Нажмите Enter для выхода в меню ')

    elif n == '3':
        '''
        если вы все данные из своего файла скопируете в файл, 
        который укажет пользователь, то это можно считать экспортом
        '''
        file_name_expott = input('Нипишите имя файла куда вы хотите скопировать данные: ')
        export_data.csv_usrer(file_name_expott)
        enter = input('Нажмите Enter для завершения')

    elif n == '4':
        '''
        считывание и сохранение, в вашу базу, записей из файла, 
        который указал пользователь
        '''
        file_name_import = input('Нипишите имя файла откуда вы хотите скопировать данные: ')
        import_data.import_user(file_name_import)
        enter = input('Нажмите Enter для завершения')

    elif n == '5':
        user_search = input('Введите имя для поиска?: ')
        searchcontact.searchcontact(user_search)
        enter = input('Нажмите Enter для завершения')
        


