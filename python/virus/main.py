from threading import Thread
from ctypes import windll
import pyautogui
import win32api
import string
import random
import time
import subprocess

def Cbeep(count: int):
    for c in range(count):
        win32api.Beep(random.randint(100,750),random.randint(100,300))

taskbar = windll.user32.FindWindowA(b'Shell_TrayWnd', None)

def ToggleTaskBar(count: int):
    for c in range(count):
        windll.user32.ShowWindow(taskbar, 0)#Hide
        time.sleep(0.2)
        windll.user32.ShowWindow(taskbar, 9)#Show

def ChangeBrightness(count: int):
    for c in range(count):
        subprocess.run(["powershell", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{str(random.randint(10,80))})"])
        time.sleep(1)
    subprocess.run(["powershell", f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{str(100)})"])
        
def msgbox():
    MessageBox = windll.user32.MessageBoxW
    random_symbols = lambda len: ''.join(random.choices([s for s in string.ascii_letters],k=len))
    MessageBox(None, f'{random_symbols(30)}\n{random_symbols(40)}', random_symbols(30), 0)

#for c in range(3):
#    msgbox()

def MoveMouse(min: int,max: int,count: int):
    for c in range(count):
        pyautogui.moveTo(random.randint(min,max),random.randint(min,max))
        time.sleep(0.1)

Thread(target=Cbeep,args=(30,)).start()
Thread(target=ToggleTaskBar,args=(30,)).start()
Thread(target=MoveMouse,args=(100,700,30)).start()
Thread(target=ChangeBrightness,args=(4,)).start()