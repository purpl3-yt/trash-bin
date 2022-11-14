import PySimpleGUI as sg
from threading import Thread
from bomber import *
sg.LOOK_AND_FEEL_TABLE['BomberTheme'] = {'BACKGROUND': '#2f2f2f',#Custom theme, thx to quuenton
'TEXT': 'white',
'INPUT': '#616161',
'TEXT_INPUT': 'white',
'SCROLL': '#616161',
'BUTTON': ('white', '#616161'),
'PROGRESS': ('#D1826B', '#CC8019'),
'BORDER': 0, 'SLIDER_DEPTH': 0,
''
'PROGRESS_DEPTH': 0}
sg.ChangeLookAndFeel('BomberTheme', True)#Apply theme

info = []
total_accounts = 0

stop=False

print('Bomber By Purpl3, Telegram: @PLNT_YT')

layout = [
[sg.Text('vaistore.gq bomber',font='Bahnschrift 15')],
[sg.HorizontalSeparator()],
[sg.Multiline(''.join(info),background_color='#2f2f2f',size=(50,13),font='Bahnschrift',key='log',autoscroll=True,no_scrollbar=True,border_width=1),sg.Push(),sg.Button('Start',key='start',font='Bahnschrift'),sg.Button('Stop',key='stop',font='Bahnschrift')],
[sg.Text('Accounts: '+str(total_accounts),font='Bahnschrift',key='log_accounts'),sg.Text('Sended reviews: '+str(total_reviews),font='Bahnschrift',key='log_reviews'),sg.Push(),sg.Text('Custom message: ',font='Bahnschrift'),sg.InputText(font='Bahnschrift',key='custom_message')]
]
window = sg.Window('B0MB3R BY D3ADC0RE',size=(720,406),layout=layout)

while True:
    event,value = window.read()

    if event == 'start':
        stop=False
        for i in range(5):#threads
            class CreateAkks(Thread):
                def run(self):
                    global total_accounts,stop
                    while True:
                        if not stop:
                            create_akk(info)
                            window['log'].update('\n'.join(info))
                            total_accounts+=1
                            window['log_accounts'].update('Accounts: '+str(total_accounts))
                        else:
                            break
            createakks_thread = CreateAkks()
            createakks_thread.start()

            class SendReviews(Thread):
                def run(self):
                    global stop
                    while True:
                        if not stop:
                            sendreviews(info,window,stop,str(value['custom_message']))
                            window['log'].update('\n'.join(info))
                        else:
                            break
            sendreviews_thread = SendReviews()
            sendreviews_thread.start()

    elif event == 'stop':
        stop=True
    
    if event == sg.WIN_CLOSED:
        stop=True
        break

window.close()