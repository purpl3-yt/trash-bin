import pyautogui as py
from random import uniform,randint
from screeninfo import get_monitors
from time import sleep as wait

py.FAILSAFE = True

monitor_x = int(get_monitors()[0].width)#get monitor width
monitor_y = int(get_monitors()[0].height)#get monitor height

def random_move():#random move mouse
    random_x = randint(10,monitor_x)#get random mouse x
    random_y = randint(10,monitor_y)#get random mouse y
    py.moveTo(random_x, random_y, uniform(2,2.4), py.easeInOutCirc)#move mouse to random cords

while True:
    wait(uniform(2,3.6))#wait 
    random_move()#move mouse
    print('Moving Cursor...')