import webbrowser
import platform,os
def clear():
    if platform.system().lower() == 'windows':
        os.system('cls')
    elif platform.system().lower() == 'linux':
        os.system('clear')

def pause():
    input('Press any key to continue! ')

sites = {
    'google':'google.com',
    'youtube':'youtube.com',
}

print('Welcome to site-redirect!')

while True:
    clear()
    site = input('Enter site to you want to open\nFor help enter "help": ')

    if site in ['help']:
        print(''.join(list(sites.keys())))
        pause()
    else:
        if site in list(sites.keys()):
            print('Open site: '+sites[site])
            webbrowser.open(sites[site])
        elif not site in list(sites.keys()):
            print('Site not be found!')

        pause()