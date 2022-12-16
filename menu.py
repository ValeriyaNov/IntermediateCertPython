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
        print('4. Импорт в json') # ?
        print('5. Экспорт')  # ?
        print('6. Поиск')  # ?
        print('7. Выход\n')   # ?
        number = input('Выберите пункт меню: ')
        controller.distribute(number, file_loger)
 
file_loger = 'loger.txt'
greeting()
menu()