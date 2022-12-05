from utils import *

cprint(r'Hello! you enter in Path-Finder, this tool created to open paths, example %appdata%')

paths = {
'appdata':os.getenv('appdata'),
'localappdata':os.getenv('localappdata'),
'temp':os.getenv('temp'),
}#You can add paths here

while True:
    s_path = cinput('For paths enter "help": ')
    if s_path in ['h','help','1','']:
        gprint(' '.join(paths))
    else:
        try:
            open(paths[str(s_path)])
            gprint('Open '+s_path+' folder')
        except KeyError:
            rprint('The path not be found!')