import controller


def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # Работает
        print('3. Скопировать данные в файл?')  # не работает хмл
        print('4. Редактировать заметку') # работает
        print('5. Поиск записи')  # поиск и вывод на экран работает
        print('6. Удаление записи')  # 

        print('7. Выход\n')   # работает
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='7':
            break
 

greeting()
menu()
