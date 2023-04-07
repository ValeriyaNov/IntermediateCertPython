import controller


def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # 
        print('3. Скопировать данные в файл?')  # 
        print('4. Сохранить в нашу базу данных?') # 
        print('5. Поиск записи')  # 
        print('6. Выход\n')   # работает
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='6':
            break
 

greeting()
menu()