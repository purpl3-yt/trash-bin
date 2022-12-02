from colorama import Fore
import os

def gprint(text):
    print(Fore.GREEN+text+Fore.RESET)

def cprint(text):
    print(Fore.CYAN+text+Fore.RESET)

def cinput(text):
    return input(Fore.CYAN+text+Fore.RESET)

def rprint(text):
    print(Fore.RED+text+Fore.RESET)

def open(path):
    os.system(f'explorer.exe {path}')
