from PIL import Image
import os,sys
import pyautogui
from glob import glob
import random
from screeninfo import get_monitors
import keyboard

os.chdir(sys.path[0])

def create_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('./screenshot.png')

    im1 = Image.open('./screenshot.png')
    width,height = int(get_monitors()[0].width),int(get_monitors()[0].height)#1920 1080

    im2 = Image.open(random.choice(glob('./tanks/tanka*.png')))
    im2 = im2.resize((int(im2.width/4),int(im2.height/4)))

    back_im = im1.copy()
    back_im.paste(im2, (int(width-im2.width-random.randint(50,width)),int(random.randint(0,height-50))), im2)
    back_im.save('./screenshot_mod.png', quality=100)

keyboard.add_hotkey('alt + shift + s', create_screenshot)
while True:
    print('To screenshot press: alt + shift + s\nFor exit press: esc')
    keyboard.wait('esc')