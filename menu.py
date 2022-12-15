import controller


def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')

def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')
        print('2. Вывод записей на экран')
        print('3. Импорт')
        print('4. Экспорт')
        print('5. Поиск')
        print('6. Выход\n')
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
 

greeting()
menu()