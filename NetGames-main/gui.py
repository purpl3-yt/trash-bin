import webbrowser
import PySimpleGUI as sg
from objects import findbyid, get_new_game,get_pop_game,find
from game_menu import GameMenu
from admin import *
sg.theme('Black')




obj_new = get_new_game()
obj_pop = get_pop_game()
pop_obj_img = []
layout = [
[sg.Image('./assets/logo.png',tooltip='NetGames'),sg.InputText('',key='search_text',font='Robot 15',tooltip='Напишите игру которую хотите найти'),sg.Image('./assets/search_ico.png',key='search_button',enable_events=True,tooltip=('Нажмите для поиска')),sg.Push(),sg.Button('Админка',font='Robot 15',key='admin',visible=False)],
[sg.HorizontalSeparator()],
[sg.Text('Popular Games',font='Robot 20'),sg.Button('      ',button_color='black',key='toggle_admin')],
[sg.HorizontalSeparator()],
]
res1 = []
count=0 

i = 0
while i < len(obj_pop):
    if i % 4 == 0 and i != 0:
        layout.append(pop_obj_img.copy()) 
        pop_obj_img.clear()
    #print(obj_pop[i].id)
    pop_obj_img.append(sg.Image(obj_pop[i].img, key=f'pop{obj_pop[i].id}', enable_events=True,tooltip=str(obj_pop[i].description).capitalize()))
    i += 1

layout.append(pop_obj_img)
layout.append([sg.HorizontalSeparator()])
layout.append([sg.Text('New Games',font='Robot 20')])
layout.append([sg.HorizontalSeparator()])
new_game = []
count=0

x = 0
while x < len(obj_new):
    if x % 4 == 0 and x != 0:
        layout.append(new_game.copy()) 
        new_game.clear()
    #print(obj_new[x].id)
    new_game.append(sg.Image(obj_new[x].img,key=f'new{obj_new[x].id}',enable_events=True,tooltip=str(obj_new[x].description).capitalize()))
    x += 1

if len(new_game) > 0:
    layout.append(new_game) 

layout.append([sg.HorizontalSeparator()])
layout.append([sg.Text('Создано: ', font='Robot 12'),sg.Button('Purpl3', font='Robot 12', key='purpl3'),sg.Text('с помощью: ', font='Robot 12'),sg.Button('Rawitti',key='rawitti',font='Robot 12')])
layout.append([sg.Text('Наш дискорд сервер: ', font='Robot 12'),sg.Button('Тут',font='Robot 12',key='server')])

window = sg.Window('NetGames',icon='./assets/Logo_big.ico',finalize=True,).Layout([[sg.Column(layout,size=(930,600), scrollable=True, vertical_scroll_only=True,sbar_trough_color='black')]])
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    elif event == 'search_button':
        if values['search_text']:
            name = values['search_text']
            games = find(name.lower())
            if games:
                GameMenu(int(games[0][0]))
        #print_all(games)
    elif event.startswith('new'): 
        event_id = f'{event[3:]}'
        obj = findbyid(int(event_id))
        #print(str(obj[0][1]).capitalize())
        GameMenu(int(event_id))
    elif event.startswith('pop'):
        event_id = f'{event[3:]}'
        obj = findbyid(int(event_id))
        GameMenu(int(event_id))
    elif event == 'toggle_admin':
        window['admin'].update(visible=True)
    elif event == 'admin':
        LoginForm()
    elif event == 'purpl3':
        webbrowser.open('https://t.me/PLNT_YT')
    elif event == 'rawitti':
        webbrowser.open('https://t.me/Rawitti')
    elif event == 'server':
        webbrowser.open('https://discord.gg/A4QQA9RgGs')
window.close()

'''
TODO:
[+] Сделать файл game_menu.py
'''
