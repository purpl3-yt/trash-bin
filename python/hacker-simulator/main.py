from time import sleep as wait
import string
import random
from colorama import Fore

random_words = [
'BRAIN',
'HACKER',
'MATRIX',
'LINUX',
'WINDOWS',
'APPLE',
'MIND',
'POWER',
'KALI_LINUX',
'HACK_WEBSITE',
'CPANEL',
'SFTP',
'FTP',
'SSH',
'CRACK',
'HACK',
'PURPL3',
'DARKNET',
'DARKWEB',
'DUCKDUCKGO']

def gprint(text):
    print(Fore.GREEN+text+Fore.RESET)

def random_string(add_power: int):
    random_len = random.randint(50,150)
    random_list = random.choices(string.ascii_letters,k=random_len)
    for i in range(add_power):
        random_item = random.randint(0,len(random_list)-1)
        random_list[random_item]+=random.choice(random_words)
    return ''.join(random_list)
    

while True:
    gprint(random_string(3))
    wait(0.001)