import csv
import json
import os
os.chdir(os.path.dirname(__file__))

'''
Здесь мы считываем и сохраняем, в нашу базу, записи из файла, 
который указал пользователь
'''


def import_csv(file_loger):
    # https://pythonworld.ru/moduli/modul-csv.html
    with open('import.csv', "a", newline='', encoding='utf-8') as file:
        fieldnames = ['Имя','Фамилия','Отчество','Дата рождения','Номер телефона','Email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(file_loger)
        # получается такой вид в файле:
        # Карала,Каронарс,Каонмморвна,1.1.1000,123456789,xdfb@zdvb.com
        print('Данные успешно сохранены в csv')


def import_json(file_loger):
    with open("import.json", "a", encoding='utf-8') as file:
        json.dump(file_loger, file, indent=2, ensure_ascii=False)
        file.write(',\n')
        print('Данные успешно сохранены в json')


def copy_cont():
    path = input('Введите файл, откуда хотите скопировать данные   ')
    def import_csv(path_to_import_csv_file): 
        data = []        
        with open(path_to_import_csv_file, "r", newline='', encoding='utf-8') as file:

            file_reader = csv.reader(file, delimiter = ",") 
            for row in file_reader:
                data.append(row)     
        return data
    d = import_csv(path)
    f = input('Введите имя или фамилию человека, данные которого необходимо записать в записную книжку   ')
    arr = []   
    for i in range(len(d)):
        if f in d[i]:
            arr.append(d[i])
    return arr



def copy_cont_json():
    path = input('Введите файл, откуда хотите скопировать данные   ')
    def import_json(path_to_import_json_file): 
        data = []        
        with open(path_to_import_json_file, "r", encoding='utf-8') as file:
            file_reader = json.load(file) 
            for i in range(0, len(file_reader)):
                g = list(file_reader[i].values())
                data.append(g)
        return data

d = import_json(path)
new = input('Введите имя или фаммилию человека, данные которого хотите записать')
arr = []
for i in range(len(d)):
    if new in d[i]:
        arr.append(d[i]) 

for i in range(len(arr)):
    with open('phonebook.csv', "a", encoding='utf-8') as fil:
        csv_fil = csv.writer(fil, delimiter=';')
        csv_fil.writerow(arr[i])


