import controller


def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')

def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран в формате json')  # Не работает
        print('3. Вывод записей на экран в формате csv')  # Работает
        print('4. Скопировать данные в файл?') # В работе
        print('5. Экспорт')  # ?
        print('6. Поиск')  # ?
        print('7. Выход\n')   # ?
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='7':
            break
 
 
path_json_data = 'import.json'  # поменять все пути на этот
path_csv_data = 'import.csv'   # поменять все пути на этот
greeting()
menu()