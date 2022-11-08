import pyautogui as py
from random import uniform,randint
from screeninfo import get_monitors
from time import sleep as wait
py.FAILSAFE = True

monitor_x = int(get_monitors()[0].width)
monitor_y = int(get_monitors()[0].height)

def random_move():
    random_x = randint(10,monitor_x)
    random_y = randint(10,monitor_y)
    py.moveTo(random_x, random_y, uniform(2,2.4), py.easeInOutCirc)

while True:
    wait(uniform(2,3.6))
    random_move()
