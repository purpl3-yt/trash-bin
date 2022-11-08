import PySimpleGUI as sg
import webbrowser
from utils import *

sg.LOOK_AND_FEEL_TABLE['FCleanerTheme'] = {'BACKGROUND': '#2f2f2f',#Custom theme, thx to quuenton
'TEXT': 'white',
'INPUT': '#616161',
'TEXT_INPUT': 'white',
'SCROLL': '#616161',
'BUTTON': ('white', '#616161'),
'PROGRESS': ('#D1826B', '#CC8019'),
'BORDER': 0, 'SLIDER_DEPTH': 0,
''
'PROGRESS_DEPTH': 0}
sg.ChangeLookAndFeel('FCleanerTheme', True)#Apply theme

def Settings():#In development
    layout = [[]]

def MainWindow():
    layout = [[
    sg.Text('FCleaner',font='"Bahnschrift SemiBold SemiConden" 18'),
    sg.Push(),
    sg.Image('./assets/settings.png',key='settings',enable_events=True)
    ],
    [sg.HorizontalSeparator()],
    [sg.Text('Glory to Ukraine',font='Bahnschrift'),sg.Button('Creator GitHub',key='github',font='Bahnschrift')],
    [sg.VPush()],   
    [],
    [],
    [],
    [],
    ]
    fill_rows(layout,sg)#Add button to the last rows in layout
        
    window = sg.Window('FCleaner - Full Cleaner',layout,size=(800,430),finalize=True,use_default_focus=False)#create main window

    while True:
        event,values = window.read()
        if event==sg.WIN_CLOSED:
            break
        
        elif event in [i for i in clean_folders.keys()]:
            if sg.PopupOKCancel('You sure? '+clean_folders[str(event)][1])=='OK':
                sg.Popup(deletefiles(clean_folders[str(event)][0]))

        elif event=='github':
            webbrowser.open('https://github.com/purpl3-yt')

        elif event=='settings':
            sg.Popup('Settings in development')

    window.close()

MainWindow()