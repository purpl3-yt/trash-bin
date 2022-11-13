import requests
import random
from bs4 import BeautifulSoup
import time
from os import system, name
import itertools
import threading
all_nicks_guley = []
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def parse_site_1():
    url = 'https://ru.nickfinder.com/deadinside'
    response = requests.get(url)
    response.encoding = 'utf-8'
    code = BeautifulSoup(response.text, 'lxml')
    parsed_nicks_guley = code.find_all('div', class_='copy_variant')

    for i in range(0, len(parsed_nicks_guley)):
        all_nicks_guley.append(parsed_nicks_guley[i].text)


def parse_site_2():
    url_gul = 'https://conterfrag.ru/niki-dlya-dota-2/'
    response_gul = requests.get(url_gul)
    response_gul.encoding = 'utf-8'
    code_gul = BeautifulSoup(response_gul.text, 'lxml')
    parsed_nicks_gul = code_gul.find_all('li')
    # print(parsed_nicks_gul[330].text)
    for i in range(25, 330):
        all_nicks_guley.append(parsed_nicks_gul[i].text)


def parse_site_3():
    url_guly = 'https://vnickname.ru/nicki-dota.php'
    response_guly = requests.get(url_guly)
    response_guly.encoding = 'utf-8'
    code_guly = BeautifulSoup(response_guly.text, 'lxml')
    parsed_nicks_guly = code_guly.find_all('td')
    for i in range(18, 340):
        all_nicks_guley.append(parsed_nicks_guly[i].text)

    url_guly1 = 'https://vnickname.ru/nicki-ta-2.php'
    response_guly1 = requests.get(url_guly)
    response_guly1.encoding = 'cp1251'
    code_guly1 = BeautifulSoup(response_guly1.text, 'lxml')
    parsed_nicks_guly1 = code_guly1.find_all('td')
    for i in range(18, 340):
        all_nicks_guley.append(parsed_nicks_guly1[i].text)

def parse_site_4():
    url_guly = 'https://vnickname.ru/nicki-grustnye.php'
    response_guly = requests.get(url_guly)
    response_guly.encoding = 'cp1251'
    code_guly = BeautifulSoup(response_guly.text, 'lxml')
    parsed_nicks_guly = code_guly.find_all('td')
    for i in range(18, 340):
        all_nicks_guley.append(parsed_nicks_guly[i].text)
    url_guly1 = 'https://vnickname.ru/nicki-grustnye-1.php'
    response_guly1 = requests.get(url_guly1)
    response_guly1.encoding = 'cp1251'
    code_guly1 = BeautifulSoup(response_guly1.text, 'lxml')
    parsed_nicks_guly1 = code_guly1.find_all('td')
    for i in range(18, 340):
        all_nicks_guley.append(parsed_nicks_guly1[i].text)

    url_guly2 = 'https://vnickname.ru/nicki-neobychnye.php'
    response_guly2 = requests.get(url_guly2)
    response_guly2.encoding = 'cp1251'
    code_guly2 = BeautifulSoup(response_guly2.text, 'lxml')
    parsed_nicks_guly2 = code_guly1.find_all('td')
    for i in range(18, 340):
        all_nicks_guley.append(parsed_nicks_guly2[i].text)

    url_guly3 = 'https://vnickname.ru/nicki-neobychnye-2.php'
    response_guly3 = requests.get(url_guly3)
    response_guly3.encoding = 'cp1251'
    code_guly3 = BeautifulSoup(response_guly3.text, 'lxml')
    parsed_nicks_guly3 = code_guly3.find_all('td')
    for i in range(18, 340):
        all_nicks_guley.append(parsed_nicks_guly3[i].text)

    url_guly4 = 'https://vnickname.ru/nicki-interesnye.php'
    response_guly4 = requests.get(url_guly4)
    response_guly4.encoding = 'cp1251'
    code_guly4 = BeautifulSoup(response_guly4.text, 'lxml')
    parsed_nicks_guly4 = code_guly4.find_all('td')
    for i in range(18, 113):
        del parsed_nicks_guly4[113];del parsed_nicks_guly4[47]
        print(parsed_nicks_guly4[i].text, i)
        all_nicks_guley.append(parsed_nicks_guly4[i].text)


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
done = False
while True:
    clear()
    print(colors.OKGREEN+colors.BOLD +'Привет это генератор крутых ников для игр'+colors.ENDC)
    choose = input(colors.OKGREEN+colors.BOLD+'Что хочешь сделать? 1) Выбрать рандомный ник, 2) Автор, 3) Сколько всего ников? 4) Выход: '+colors.ENDC)
    if choose=='1':
        clear()
        if done == False:
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    print(colors.OKGREEN+colors.BOLD+'\rПарсим ' + c+'\n'+colors.ENDC)
                    time.sleep(0.1)
            t = threading.Thread(target=animate)
            t.start()
            parse_site_1()
            parse_site_2()
            parse_site_3()
            parse_site_4()
            done = True
            clear()
            print(colors.OKGREEN+colors.BOLD+'Внимание есть кривые ники например с непонятными символами и т.д!'+colors.ENDC)
            print(colors.OKGREEN+colors.BOLD+all_nicks_guley[random.randint(0,len(all_nicks_guley))]+colors.ENDC)
            while True:
                repeat = input(colors.OKGREEN+colors.BOLD+'Вы хотите сделать еще один ник? 1) Да 2) нет: '+colors.ENDC)
                if repeat == '1':
                    clear()
                    print(colors.OKGREEN+colors.BOLD+all_nicks_guley[random.randint(0,len(all_nicks_guley))]+colors.ENDC)
                if repeat == '2':
                    break
        elif done == True:
            print(colors.OKGREEN+colors.BOLD+all_nicks_guley[random.randint(0,len(all_nicks_guley))]+colors.ENDC)
            repeat = input(colors.OKGREEN+colors.BOLD+'Вы хотите сделать еще один ник? 1) Да 2) нет: '+colors.ENDC)
            if repeat == 1:
                print(colors.OKGREEN+colors.BOLD+all_nicks_guley[random.randint(0,len(all_nicks_guley))]+colors.ENDC)
                pass
            elif repeat == 2:
                pass
            else:
                print(colors.OKGREEN+colors.BOLD+all_nicks_guley[random.randint(0,len(all_nicks_guley))]+colors.ENDC)
    

    if choose=='2':
        clear()
        print(colors.OKGREEN+colors.BOLD+'Автор: Purpl3 (Я сделал эту программу по приколу ну и проптиковаться в парсерах удачно использования)\n'+colors.ENDC)
        temp = input(colors.OKGREEN+colors.BOLD+'Нажмите enter для продолжения: '+colors.ENDC)
        if temp == 1:
            pass
        else:
            pass
    if choose=='3':
        clear()
        if done==False:
            print(colors.OKGREEN+colors.BOLD+'Перед тем как узнать количество ников вам надо их спарсить нажмите enter а потом цифру 1 и после этого зайдите сюда еще раз \n'+colors.ENDC)
            temp = input(colors.OKGREEN+colors.BOLD+'Нажмите enter для продолжения: '+colors.ENDC)
            if temp == 1:
                pass
            else:
                pass
        else:
            print(colors.OKGREEN+colors.BOLD+f'Всего ников: {len(all_nicks_guley)}\n'+colors.ENDC)
            temp = input(colors.OKGREEN+colors.BOLD+'Нажмите enter для продолжения: '+colors.ENDC)
            if temp == 1:
                pass
            else:
                pass
    if choose=='4':
        quit()