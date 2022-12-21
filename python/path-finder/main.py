from utils import *

cprint(r'Hello! you enter in Path-Finder, this tool created to open paths, example %appdata%')

paths = {
'appdata':os.getenv('appdata'),
'localappdata':os.getenv('localappdata'),
'temp':os.getenv('temp'),
'recent':f'{os.getenv("USERPROFILE")}\AppData\Roaming\Microsoft\Windows\Recent'
}#You can add paths here

while True:
    s_path = cinput('For paths enter "help": ')
    if s_path in ['h','help','1','']:
        gprint('\n'.join(paths))
    else:
        try:
            open(paths[str(s_path)])
            gprint('Open '+s_path+' folder')
        except KeyError:
            rprint('The path not be found!')