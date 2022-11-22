import os,platform
from dialogs import *
from colorama import Fore

def cls():
    if platform.system().lower() == 'windows':
        os.system('cls')
    elif platform.system().lower() == 'linux':
        os.system('clear')

def gprint(text):
    print(Fore.GREEN+text+Fore.RESET)

gprint('Hello! its text formater')

while True:
    text = input(Fore.GREEN+'Enter your text: '+Fore.RESET)
    mode = input(Fore.GREEN+'Enter mode (for help enter "help"): '+Fore.RESET)
    if str(mode).lower() in ['h','help','р']:
        print(Fore.CYAN+generate_help()+Fore.RESET)

    else:
        func = getattr(funcs, modes_list.index(mode))
        result = func(text)
        print(Fore.CYAN+result+Fore.RESET)