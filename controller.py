import operations
import export_data
import import_data


def distribute(n, file_loger):
    #file_loger = 'loger.txt'
    if n == '1':
        operations.new_contact()  # переходим в operations
        enter = input('Нажмите Enter для завершения')
        #menu()
    elif n == '2':
        filecontents = operations.read_file(file_loger)
        if len(filecontents) == 0:
            print('Записей нет')
        else:
            print(filecontents)
        enter = input('Нажмите Enter для завершения')
        #menu()
    elif n == '3':
        import_data.import_csv(file_loger)
        print('Данные успешно конвертированы в csv')
        enter = input('Нажмите Enter для завершения')
    elif n == '4':
        file_temp = operations.read_file(file_loger)
        file_csv = import_data.import_json(file_temp)
        operations.write_to_file('import.json', file_csv)
        enter = input('Нажмите Enter для завершения')
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

