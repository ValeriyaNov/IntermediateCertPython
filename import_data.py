import csv


'''
Здесь мы считываем и сохраняем, в нашу базу, записи из файла, 
который указал пользователь
'''
def import_user():

    print()





'''
Удалить после того как все заработает

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
'''

'''
# код от Валерии
def import_csv(path_to_import_csv_file): 
    data = []        
    with open(path_to_import_csv_file, "r", newline='', encoding='utf-8') as file:
    
        file_reader = csv.DictReader(file, delimiter = ";") 
        for row in file_reader:
            data.append(row)     
    return data

def import_json(file_loger):
    data = []      
    with open('import.json', 'r', encoding='UTF-8') as file: 
        data = json.load(file) 
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)
    #return data
'''


