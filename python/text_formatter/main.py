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

def cprint(text):
    print(Fore.CYAN+text+Fore.RESET)

def rprint(text):
    print(Fore.RED+text+Fore.RESET)

def getmode():
    return input(Fore.GREEN+'Enter mode (for help enter "help"): '+Fore.RESET)

def gettext():
    return input(Fore.GREEN+'Enter your text: '+Fore.RESET)

gprint('Hello! its text formater')

err_mode = False

while True:
    if not err_mode:
        text = gettext()
    mode = getmode()
    if str(mode).lower() in ['h','help','р']:
        cprint(generate_help())
    else:
        try:
            func = getattr(funcs, modes_list[modes_list.index(mode)])
        except ValueError:
            rprint('No such mode: '+mode)
            err_mode=True
        else:
            err_mode=False
            result = func(text)
            if type(result) == list:
                cprint('\n'.join(result))
            elif type(result) == str:
                cprint(result)