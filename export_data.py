import csv
import json


def csv_to_data(file_name='database.csv'):
    with open(file_name, "r", newline='', encoding='utf-8') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data


def csv_to_csv(user_file_name, data=csv_to_data()):
    csvArray = csv_to_data()
    
    with open(f"{user_file_name}.csv", "w", newline='', encoding='utf-8') as bd:
        
        bdd = csv.writer(bd, delimiter = ",", lineterminator="\r")
        for i in csvArray:
            
            bdd.writerow(i)


# работает
def csv_to_json(jsonFilePath, csvFilePath='database.csv'):

    jsonArray = csv_to_data()
    with open(f"{jsonFilePath}.json", 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
        
        

