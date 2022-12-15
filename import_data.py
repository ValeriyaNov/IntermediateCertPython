import csv
import json
import operations


def import_csv(file_loger): 
    
    with open('import.csv', "a", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(file_loger)
    

'''
def import_csv(path_to_import_csv_file): 
    data = []        
    with open(path_to_import_csv_file, "r", newline='', encoding='utf-8') as file:
    
        file_reader = csv.DictReader(file, delimiter = ";") 
        for row in file_reader:
            data.append(row)     
    return data
'''

def import_json(path_to_import_json_file):
    data = []      
    with open(path_to_import_json_file, 'r', encoding='UTF-8') as file: 
        data = json.load(file) 
        for i in range(0, len(data)): 
            d1 = {'contact_id': ''}
            data[i], d1 = d1, data[i]
            data[i].update(d1)
    return data

'''
def convert_txt_csv(file):
    #file = open("Date.txt")
    i = 0
    #with open('data.csv', 'w', newline='') as csvF:
        writer = csv.writer(file, delimiter=";")
        while i < 10:
            href = file.readline()
            writer.writerow([href])
            #print(href)
            i = i + 1
'''

if __name__ == "__main__":
    from pprint import pprint
    #path_to_import_json_file = 'import.json'
    #path_to_import_csv_file = 'import.csv'

