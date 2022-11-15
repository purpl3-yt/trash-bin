import shutil
from assets.img_gen import *
import PySimpleGUI as sg
from objects import *
import os
from time import sleep as delay
sg.theme('black')

game_info = None

def AddPopup():

    genres = get_all_data_genre()
    genres_list = []
    for i in genres:
        genres_list.append(str(i.getid())+' '+str(i.getname()).capitalize())
    

    layout = [ # For edit
    [sg.Text('Name: '), sg.InputText('', key='input_name')],
    [sg.Text('Genre: '), sg.InputCombo(genres_list,key='input_genres',readonly=True)],
    [sg.Text('Type: '), sg.InputText('', key='input_type')],
    [sg.Text('Description: '), sg.Multiline('', key='input_desc',size=(50,6))],
    [sg.Text('Year: '), sg.Text('     '),sg.CalendarButton('Date', key='input_year',format='%Y'),sg.Push()],
    [sg.Text('Systemrequirements: '), sg.InputText('', key='input_systemrequire')],
    [sg.Text('Cost: '), sg.InputText('', key='input_cost')],
    [sg.Text('Img Path: '),sg.Input(key='_FILEBROWSE_', enable_events=True, visible=True),sg.FileBrowse('Обзор',enable_events=True,target='_FILEBROWSE_'),sg.Push()],
    [sg.Image(key='preview')],
    [sg.Text('Gamelink: '), sg.InputText('', key='input_gamelink')],
    [sg.Button('Сохранить',key='save'),sg.Button('Выйти',key='exit')],
    [sg.Text('',key='log')]]

    window = sg.Window('Edit Menu',layout)

    while True:
        event,value = window.read()

        if event == sg.WIN_CLOSED or event == 'exit':
            break
        elif event == '_FILEBROWSE_':
            convert_image(value['_FILEBROWSE_'])
            window['preview'].update(source=tempfile.gettempdir()+'temp.png')
            
        elif event == 'save':
            img_path = value['_FILEBROWSE_']
            getfilename = str(img_path).rfind('/')
            shutil.copy(img_path, './assets/')
            create_image('./assets/'+img_path[getfilename:],value['input_name'])
            game_to_add = Game(value['input_name'],value['input_genres'][:1],value['input_type'],value['input_desc'],value['input_year'],value['input_systemrequire'],value['input_cost'],0.0,f'./assets/{value["input_name"]}',value['input_gamelink'])
            adddb(game_to_add)
            window['log'].update('Информация сохранилась!')
    if os.path.isfile(tempfile.gettempdir()+'temp.png'):
        os.remove(tempfile.gettempdir()+'temp.png')
    window.close()

def GetAllPopup():
    
    game_ids = get_all_id()
    games_inputcombo = []
    for i in game_ids:
        game_info = findbyid(i)
        games_inputcombo.append(f'{str(i)} ({str(game_info.getname()).capitalize()})')

    layout = [
    [sg.Text('Выберите айди игры: '),sg.InputCombo(games_inputcombo, key='select',readonly=True),sg.Push(),sg.Text('Режим редактирования',visible=False,key='edit_mode')],
    [sg.Text('',key='info')],
   
    [sg.Button('Получить инфу',key='confirm',font='Robot 12'),sg.Button('Редактировать',font='Robot 12',visible=False,key='edit')]
    ]

    window = sg.Window('Игра по айди',layout)

    

    while True:
        event, value = window.read()

        if event == 'confirm':
            if value['select']!='':
                

                game_info = findbyid(int(value['select'][:2]))

                def edit_menu():
                    
                    layout = [ # For edit
        [sg.Text('Name: '), sg.InputText(game_info.getname(), key='input_name')],
        [sg.Text('Type: '), sg.InputText(game_info.gettype(), key='input_type')],
        [sg.Text('Description: '), sg.InputText(game_info.getdescription(), key='input_desc')],
        [sg.Text('Year: '), sg.InputText(game_info.getyear(), key='input_year')],
        [sg.Text('Systemrequirements: '), sg.InputText(game_info.getsystemrequirements(), key='input_systemrequire')],
        [sg.Text('Cost: '), sg.InputText(game_info.getcost(), key='input_cost')],
        [sg.Text('Likes: '), sg.InputText(game_info.getlikes(), key='input_likes')],
        [sg.Text('Img Path: '), sg.InputText(game_info.getimg(), key='input_img')],
        [sg.Text('Gamelink: '), sg.InputText(game_info.getgamelink(), key='input_gamelink')],
        [sg.Button('Сохранить',key='save'),sg.Button('Выйти',key='exit')],
        [sg.Text('',key='log')]]

                    window = sg.Window('Edit Menu',layout)

                    while True:
                        event,value = window.read()

                        if event == sg.WIN_CLOSED or event == 'exit':
                            break
                        elif event == 'save':
                            
                            update(game_info,value['input_name'],value['input_type'],value['input_desc'],value['input_year'],value['input_systemrequire'],value['input_cost'],value['input_likes'],value['input_img'],value['input_gamelink'])
                            window['log'].update('Информация сохранилась!')
                    window.close()

                

                window['edit'].update(visible=True) 
                window['info'].update(f'''
ID: {game_info.getid()}
Name: {game_info.getname()}
Genres: {str(game_info.getgenres())}
Type: {game_info.gettype()}
Description: {game_info.getdescription()}
Year: {game_info.getyear()}
Systemrequirements: {game_info.getsystemrequirements()}
Cost: {game_info.getcost()}
Likes: {game_info.getlikes()}
Img: {game_info.getimg()}
Gamelink: {game_info.getgamelink()}
''')
            else:
                window['info'].update('Выберите айди игры!')
        if event == sg.WIN_CLOSED:
            break
    
        elif event == 'edit':
            edit_menu()
        elif event == 'save':
            window['info'].update(visible=True)
            window['edit_mode'].update(visible=False)
    window.close()

def DeletePopup():

    game_ids = get_all_id()
    games_inputcombo = []
    for i in game_ids:
        game_info = findbyid(i)
        games_inputcombo.append(f'{str(i)} ({str(game_info.getname()).capitalize()})')

    layout = [
    [sg.Text('Выберите айди игры: '),sg.InputCombo(games_inputcombo, key='select',readonly=True)],
    [sg.Text('',key='info')],
    [sg.Button('Удалить игру',key='confirm')]
    ]

    window = sg.Window('Игра по айди',layout)

    while True:
        event, value = window.read()

        if event == 'confirm':
            if value['select']!='':
                game_info = findbyid(int(value['select'][:1]))
                window['info'].update(f'Удалена игра: {str(value["select"][:1])}\nС названием: {str(game_info.getname()).capitalize()}')
                delete(findbyid(int(value['select'][:1])))
            else:
                window['info'].update('Выберите айди игры!')
        if event == sg.WIN_CLOSED:
            break
    window.close()



def AdminMenu():
    layout = [
    [sg.VerticalSeparator(),sg.Button('<-- Назад',key='back',font='Robot 15'),sg.Push(),sg.Text('Админка', font='Robot 15'),sg.Push(),sg.VerticalSeparator()],
    [sg.HorizontalSeparator()],
    [sg.Button('Добавить игру в DB',key='add_games',font='Robot 15'),sg.Button('Посмотреть игры',key='get_games',font='Robot 15'),sg.Button('Удалить игру',key='delete_games',font='Robot 15')],
    [sg.VPush()],
    [sg.Text('', font='Robot 12',key='logs'),sg.Push()]]

    window = sg.Window('Admin',layout, size=(980,620),finalize=True)
    
    while True:
        event, value = window.read()

        if event == sg.WIN_CLOSED or event == 'back':
            break

        elif event == 'add_games':
            AddPopup()
        elif event == 'get_games': 
            GetAllPopup()
        elif event == 'delete_games':
            DeletePopup()

    window.close()

def LoginForm():
    layout = [[sg.Text('Введите логин: '),sg.InputText(key='login_input')],
    [sg.Text('Введите пароль: '),sg.InputText(password_char='*',key='password_input')],
    [sg.Text('',key='log')],
    [sg.Button('Войти',key='enter')]]

    window = sg.Window('Login Form',layout)
    credentials = False
    while True:
        event,value = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'enter':
            if value['login_input']=='' or value['password_input']=='':
                window['log'].update('Введите логин или пароль!!!')
            elif tryenter(value['login_input'],value['password_input']):
                credentials=True
                break
            else:
                window['log'].update('Неправильно!!!')
    window.close()
    if credentials:
        AdminMenu()
#AdminMenu()