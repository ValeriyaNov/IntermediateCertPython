import operations
import export_data
import import_data

#file_loger = 'loger.txt'

def distribute(n, file_loger):
    if n == '1':
        temp = operations.new_contact()  # переходим в operations
        import_data.import_csv(temp)
        import_data.import_json(temp)
        enter = input('Нажмите Enter для завершения')
    elif n == '2':
        operations.read_json()
        #if len(filecontents) == 0:
        #    print('Записей нет')
        #else:
        #    print(filecontents)
        enter = input('Нажмите Enter для завершения')
    elif n == '3':
        operations.read_csv()
        enter = input('Нажмите Enter для завершения')
    elif n == '4':
        file_temp = operations.read_file(file_loger)
        file_csv = import_data.import_json(file_temp)
        operations.write_to_file('import.json', file_csv)
        enter = input('Нажмите Enter для завершения')
    elif n == '5':
        #searchcontact()
        enter = input('Нажмите Enter для завершения')
        #menu()
    else:
        print('Пожалуста, введите номер пункта меню')
        enter = input('Нажмите Enter для завершения')
        #menu()

