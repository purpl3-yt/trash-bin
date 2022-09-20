import PySimpleGUI as sg
from random import randint as ran
from playsound import playsound
sg.theme('DarkAmber')
layout = [  [sg.Text('Привет это бен')],
            [sg.Text('Спроси что-то у бена'), sg.InputText(key='question',do_not_clear=False),],
            [sg.Button('Спросить', key='play'), sg.Button('Выйти')],
            [sg.T('', text_color='white', size=(50,1), key='output')]]
def write(line):      
        window['output'].update(line)
def response():
    random_num = ran(1,4)
    if random_num==1:
        write('Да')
        playsound('./yes.mp3')
    elif random_num==2:
        write('Нет')
        playsound('./no.mp3')
    elif random_num==3:
        write('Хохохо')
        playsound('./hohoho.mp3')
    elif random_num==4:
        write('*Звук смачного рыга*')
        playsound('./foo.mp3')

window = sg.Window('Бен', layout,finalize=True)
window['question'].bind("<Return>", "_Enter")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выйти':
        break
    if event == 'play':
        response()
    elif event == 'question_Enter':
        response()
