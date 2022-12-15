import operations
import export_data
import import_data


def distribute(n):
    
    if n == '1':
        operations.new_contact()  # переходим в operations
        enter = input('Нажмите Enter для завершения')
        #menu()
    elif n == '2':
        #myfile = open(filename, 'r+')
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print('Записей нет')
        else:
            print(filecontents)
        #myfile.close
        enter = input('Нажмите Enter для завершения')
        menu()
    elif n == '5':
        #searchcontact()
        enter = input('Нажмите Enter для завершения')
        menu()
    elif n == '6':
        print('Спасибо за просмотр')
    else:
        print('Пожалуста, введите номер пункта меню')
        enter = input('Нажмите Enter для завершения')
        menu()

