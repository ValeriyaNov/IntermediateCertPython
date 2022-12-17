import operations
import export_data
import import_data


def distribute(n):
    if n == '1':
        temp = operations.new_contact()  # переходим в operations
        #import_data.import_csv(temp)
        #import_data.import_json(temp)
        enter = input('Нажмите Enter для завершения')
    elif n == '2':
        print('Выберите формат отображения данных: 1 - Построчно; 2 - В одну строку', sep = '\n')
        num = int(input())
        if num == 1 or num == 2:
            read_contact(num)
        enter = input('Нажмите Enter для выхода в меню ')
    elif n == '3':
        operations.read_csv()
        enter = input('Нажмите Enter для завершения')
    elif n == '4':
        file_name_expott = input('Нипишите имя файла куда вы хотите скопировать данные: ')
        #export_data.path_json_data(file_name_expott)
        enter = input('Нажмите Enter для завершения')
    elif n == '5':
        #searchcontact()
        enter = input('Нажмите Enter для завершения')
        #menu()
    #else:
    #    print('Пожалуста, введите номер пункта меню')
    #    enter = input('Нажмите Enter для завершения')
        #menu()

