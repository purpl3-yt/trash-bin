import random
import string
import sys,os
from threading import Thread
import webbrowser
from termcolor import *
from time import sleep
from datetime import datetime
import playsound
from gtts import gTTS

def hackerstr(lenght):
    from random import choice
    symbols = ['a','b','c','d','e','i','g']
    hackerstr = ''
    for i in range(0,int(lenght)):
        hackerstr+=choice(symbols)
    return hackerstr

print('Для старта напишите "Старт бравл стронг"')
start_str = input('Brawl strong: ')
if str(start_str).lower().startswith('старт бра'):
    print('Бравл стронг активирован')
else:
    print('Неправильный бравл')
    sys.exit()

def start():
    print('Добрый день')
    sleep(1)
    print('Текущее время: '+datetime.now().strftime('%H:%M'))
    sleep(1)
    while True:
        os.system('cls')
        print('''
1) Взломать Пентагон
2) Засрать твой рабочий стол
3) Бан 
4) Звук взрывного пердежа
5) Версия бравл стронга
6) Озвучить текст
''')
        sel = input('')
        if sel == '1':
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            pass
        elif sel == '2':
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
            for i in range(0,60):  
                random_symbols = string.ascii_lowercase
                with open(desktop+f'\\{hackerstr(random.randint(3,12))}.txt','w') as ponok:
                    ponok.write(f'Бравл стронг топ!!!!!\n{"".join(random.choices(random_symbols,k=100))}')
                    ponok.close()
            pass
        elif sel == '3':
            os.system('shutdown /s')
        elif sel == '4':
            class Perdesh(Thread):
                 def run(self):
                    playsound.playsound('./perdesh.mp3')
            start_sound = Perdesh()
            start_sound.start()
        elif sel == '5':
            print('Версия бравл стронга')
            sleep(0.5)
            phrases = ['0.0.1','beta','alpha','pro','test','premium','vip']
            for i in phrases:
                print(i)
                sleep(0.1)
            os.system('pause')
            pass
        elif sel == '6':
            words = input('Введите слова: ')
            tts = gTTS(str(words),lang='ru')
            tts.save('voice.mp3')
            playsound.playsound('voice.mp3')
            os.remove('voice.mp3')
start()