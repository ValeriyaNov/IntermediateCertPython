import controller


def greeting():
    print()
    print('<Записная книга>')


def menu():
    while True:
        print('\nМЕНЮ')
        print('1. Добавить новую запись')  
        print('2. Вывод записей на экран')  
        print('3. Скопировать данные в файл?')  
        print('4. Редактировать заметку') 
        print('5. Поиск записи')  
        print('6. Удаление записи')   

        print('7. Выход\n')   
        number = input('Выберите пункт меню: ')
        controller.distribute(number)
        if number =='7':
            break
 

greeting()
menu()
