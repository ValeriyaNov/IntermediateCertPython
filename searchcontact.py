

# Поиск по id
def search_id(id):
    
    myfile = open('database.csv', 'r', encoding='utf-8')
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        linelst = line.split(';')
        if len(linelst) < 5: break
        
        found = 0
        print(id, type(id))
        print(linelst[0], type(linelst[0]))
        if str(linelst[0]) == str(id):
            print('Результат поиска: ', end = ' ')
            print( line)
            found = found+1
            
    if found == 0:
        print('Заметка с таким id не найдена...') 
    return line

# Поиск по name
def search_name(name):
    
    myfile = open('database.csv', 'r+', encoding='utf-8')
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if name in line:
            print('Результат поиска: ', end = ' ')
            print( line)
            found = True
            break
    if found == False:
        print('Заметка с таким заголовком не найдена...') 
    return line

def search_date(date):
    #print(type(date))
    #print(date)
    myfile = open('database.csv', 'r+', encoding='utf-8')
    filecontents = myfile.readlines()
    
    found = False
    for line in filecontents:
        linelst = line.split(";")
    
        if len(linelst) < 5: break
        
        found = 0
        if linelst[3] == date:
            print('Результат поиска: ', end = ' ')
            print( line)
            found = found + 1

            
    if found == 0:
        print('Заметка по введенной дате не найдена...') 
    
        
    return line