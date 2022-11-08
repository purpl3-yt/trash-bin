import PySimpleGUI as sg

sg.theme('Black')

layout = [[sg.Text('aaaa'),sg.Button('Close',key='close')]]

window = sg.Window('Test window', layout)

while True:
    event,value = window.read()

    if event == sg.WIN_CLOSED or event == 'close':
        break
    window.close()