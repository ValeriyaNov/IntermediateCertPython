import operations
#import export_data
#import import_data


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
        file_name_expott = input('Нипишите имя файла куда вы хотите скопировать данные: ')
        
        enter = input('Нажмите Enter для завершения')
    elif n == '4':
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

