import csv
import import_data
import json
import os
os.chdir(os.path.dirname(__file__))
import csv
import datetime
import pandas as pd
import searchcontact


# Создаем новую заметку
def new_contact():
    id = input_id()
    name_note = input('Заголовок: ')
    body_note = input('Тело заметки: ')
    data_day = datetime.date.today()
    data_minute = datetime.datetime.now().time()
    new_list= [id, name_note, body_note, data_day, data_minute]
    save_to_csv(new_list)

    print('Заметка успешно сохранена')


# Вводим id
def input_id():

    input_id = input('Введите id ')
    while not input_id.isdigit():
        print('Ошибка. Не корректный id')
        input_id = input('Введите id ')
    with open('database.csv', "r", newline='', encoding='utf-8') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            if len(row)==1:
                continue
            else:
                data.append(row)
    #print(data)
    flag = False
    while flag == False:
        for line in data:
            
            i = 0
            a = line[0]
            flag = True
            if input_id == a:
                print('Ошибка. Не корректный id ')
                input_id = input('Введите id ')
                flag = True
            else: 
                flag = True
            i = i+1
            
    return input_id





# Сохраняем в csv
def save_to_csv(new_note, file_name = 'database.csv'):
    with open(file_name, "a", newline='', encoding='utf-8') as bd:
        for i in range(len(new_note)):
            if i != len(new_note) - 1:
                bd.write(f'{new_note[i]};')
            else:
                bd.write(f'{new_note[i]}')
        bd.write('\n')


# Читаем csv
# Читаем csv
def read_contact(unit = 1, file_name = 'database.csv'):
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()


def redact_notes(id):
    df = pd.read_csv("database.csv")
    df.head(5)
    searchcontact.search_id(id)
    new_body = input("Задайте новое значение в теле заметки")
    df.loc[df["id"]==id, "тело заметки"] = new_body
    print("Заметка сохранена")




#import os
#print (os.listdir(os.getcwd()))
#new_contact()