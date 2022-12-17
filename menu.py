import controller


def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')

def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # В работе
        print('3. Импорт')  # В работе
        print('4. Скопировать данные в файл?') # В работе
        print('5. Поиск')  # ?
        print('6. Выход в меню\n')  # ?
        print('7. Выход\n')   # ?
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='7':
            break
 
 
path_json_data = 'import.json'  # поменять все пути на этот
path_csv_data = 'import.csv'   # поменять все пути на этот
filename = 'phonebook.csv'
greeting()
menu()