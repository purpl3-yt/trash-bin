import shutil
from threading import Thread
import PySimpleGUI as sg
from objects import findbyid, get_download_path,pathtofile, updatelikes
import urllib.request
import os,sys
sg.theme('Black')

def GameMenu(gameid):
    game_info = findbyid(gameid)
    key_star = 1
    stars = []
    stars.append(sg.Text('Платформы: '+game_info.getsystemrequirements(),font='Robot 12'))
    stars.append(sg.Push())
    #if len(str(findbyid(gameid)[4])) > :
    
    if game_info.getlikes() == 0.0:
        for i in range(0, 5):
            stars.append(sg.Image('.\\assets\\star_transparent.png', key=f'star{key_star}',enable_events=True))
            key_star += 1
    else:
        liks_float = game_info.getlikes()%1
        likes = int(game_info.getlikes())
        temp = 5-likes
        if liks_float != 0.0:
            temp -= 1 
        for i in range(0,likes):
            stars.append(sg.Image('.\\assets\\star.png', key=f'star{key_star}',enable_events=True))
            key_star += 1
            
        if liks_float != 0.0:
            stars.append(sg.Image('.\\assets\\star_half.png', key=f'star{key_star}',enable_events=True))
            key_star += 1
        for i in range(0, temp):
            stars.append(sg.Image('.\\assets\\star_transparent.png', key=f'star{key_star}',enable_events=True))
            key_star += 1

            
        
    column_layout = [
    [sg.HorizontalSeparator()],
    [sg.Image(game_info.getimg())],
    [sg.Text(str(game_info.getdescription()).capitalize(),font='Robot 16')],
    [sg.Text('Год: '+str(game_info.getyear()),font='Tahoma 12'),sg.Text('Графика: '+str(game_info.gettype()),font='Tahoma 12'),sg.Text('Цена: '+str(game_info.getcost())+'₴',font='Tahoma 12'),sg.Push(),sg.Button('Назад',font='Robot 15',key='back'),sg.Button('Скачать',font='Robot 15',key='download')],
    stars,
    [sg.HorizontalSeparator()]]
    
    

    layout = [
    [sg.VPush()],
    [sg.Push(),sg.VerticalSeparator(),sg.Column(column_layout, scrollable=False,element_justification='c'),sg.VerticalSeparator(),sg.Push()],
    [sg.VPush()]]
    window = sg.Window('Game Menu',layout,size=(980,620),icon=pathtofile('.\\assets\\downloads.png'))
    

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'back': 
            break
        #print('You entered ', values[0])
        if event == 'download':
            filename = str(game_info.getgamelink())[::-1]
            find = filename.find('/')
            final = '/'+filename[0:find][::-1].replace('%20',' ')
            if not os.path.exists(f"{os.path.join(os.path.expanduser('~'), 'Downloads')}{final}"):
                class GetGame(Thread):
                    def run(self):
                        if os.name != 'nt':
                            urllib.request.urlretrieve(game_info.getgamelink(), final[1:])
                            shutil.move(sys.path[0]+final, f"{os.path.join(os.path.expanduser('~'), 'Downloads')}")
                        elif os.name == 'nt':
                            urllib.request.urlretrieve(game_info.getgamelink(), final[1:])
                            shutil.move(sys.path[0]+final, get_download_path())
                download_game = GetGame()
                download_game.start()
                choice, _ = sg.Window('Оповещение', [[sg.T('Игра скачалась в папку загрузки!')], [sg.Button('Ок')]], disable_close=False).read(close=True)
            else:
                choice, _ = sg.Window('Оповещение', [[sg.T('Игра уже есть в загрузках!')], [sg.Button('Ок')]], disable_close=False).read(close=True)
        
        elif event.startswith('star'):
            updatelikes(int(event[4:]),game_info)
    window.close()


'''
TODO:
[+] Сделать тут окно как в картинке game_menu.png через sg.column и добавить лайки год а справа будет описание и кнопка загрузки
[+] Через requests сделать запрос на сайт чтобы скачать игру
[+] И в базе сделать ссылку на игру
[+] Сделать поддержку загрузки игр для windows
'''