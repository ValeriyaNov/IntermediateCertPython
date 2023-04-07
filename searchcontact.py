

# Поиск по id
def search_id(id):
    
    myfile = open('database.csv', 'r+', encoding='utf-8')
    filecontents = myfile.readlines()

    found = False
    for line in filecontents:
        if id in line:
            print('Результат поиска: ', end = ' ')
            print( line)
            found = True
            break
    if found == False:
        print('Заметка с найденым id не найдена...', id) 
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
        print('Заметка с таким именем не найдена...', name) 
    return line