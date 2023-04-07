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



def export_to_xml(user_file_name, data=csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<notes>\n'
    for row in data:
        id, name, body, date, time = row
        xml += '    <note>\n'
        xml += '        <ID>{}</ID>\n' \
            .format(id)
        xml += '        <NAME>{}</NAME>\n' \
            .format(name)
        xml += '        <BODY>{}</BODY>\n' \
            .format(body)
        xml += '        <DATE>{}</DATE>\n' \
            .format(date)
        xml += '        <TIME>{}</TIME>\n' \
            .format(time)
        xml += '    </note>\n'
    xml += '</notes>'
    with open(f'{user_file_name}.xml', 'w', encoding='utf-8') as page:

        page.write(xml)
    return data


# работает
def csv_to_json(jsonFilePath, csvFilePath='database.csv'):

    jsonArray = csv_to_data()
    with open(f"{jsonFilePath}.json", 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)
        '''
        Если sure_ascii имеет значение true (по умолчанию), 
        в выводе гарантированно будут экранированы все входящие символы, отличные от ASCII. 
        Если sure_ascii имеет значение false, эти символы будут выводиться как есть.  
        '''

