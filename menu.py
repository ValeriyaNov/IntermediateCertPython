import controll
import os
os.chdir(os.path.dirname(__file__))

def greeting():
    print()
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  # Работает
        print('2. Вывод записей на экран')  # выводит в терминал
        print('3. Скопировать данные в файл?')  # сделала копирование из csv in csv
        print('4. Сохранить в нашу базу данных?') # сделано
        print('5. Поиск записи')  # работает
        print('6. Выход\n')   # работает
        number = input('Выберите пункт меню: ')
        controll.distrib(number)
         
        if number =='6':
            break
 
greeting()
menu()