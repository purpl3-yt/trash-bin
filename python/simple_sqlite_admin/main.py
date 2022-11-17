import PySimpleGUI as sg
from sqlite import *

sg.theme('Black')

layout = [
[sg.Text('Login: ',font='Bahnschrift'),sg.Input(key='login',font='Bahnschrift')],
[sg.Text('Password: ',font='Bahnschrift'),sg.Input(key='password',font='Bahnschrift')],
[sg.Text(key='log',font='Bahnschrift')],
[sg.Button('Enter',font='Bahnschrift',key='start')]]

window = sg.Window('Simple sqlite3 login',layout)

while True:
    event,value = window.read()

    if event in [sg.WIN_CLOSED]:
        break

    if event == 'start':
        if str(value['login'])=='':
            window['log'].update('Enter login!')
        elif str(value['password'])=='':
            window['log'].update('Enter password!')
        else:
            work = tryenter(str(value['login']),str(value['password']))
            if work:
                sg.Popup('Right!')
            elif not work:
                sg.Popup('Wrong!')
window.close()