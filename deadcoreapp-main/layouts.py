import PySimpleGUI as sg
tab_cheats_minecraft_layout = [sg.Button('Celestyal')]
sg.theme('Black')
tab_app_layout = [[sg.Text('Тут проги')],
[sg.Button('FlameShot',tooltip='Прога для скринов',key='flameshot'),sg.Button('KDE connect',tooltip='Управление пк с телефона',key='kdeconnect'),sg.Button('Kdenlive',tooltip='Замена Premiere Pro',key='kdenlive'),sg.Button('Google Picasa',tooltip='Просмотр фотографий',key='picasa')],
[sg.Button('Atom',tooltip='Замена PyCharm или VS Code',key='atom'),sg.Button('Blender',tooltip='Прога для 3д моделирования',key='blender'),sg.Button('https://photopea.com/',tooltip='Фотошоп онлайн без регистрации и смс и номера телефона',key='photopea'),sg.Button('BleachBit',tooltip='Скачать CCleaner без вирусов',key='bleach')],
[sg.Button('QuickCPU',key='quickcpu',tooltip='Программа которая поможет разогнать процессор (только не делайте много а то может начать троттлить или плохеть материнской плате)')]]

tab_games_layout = [[sg.Text('Тут игры')],
[sg.Button('Just Shapes & Beats',key='jseb',tooltip='Уворачиваться от шариков и квадратов.com'),sg.Button('The Long Dark',key='thelongdark', tooltip='Выживи в лесу челлендж'),sg.Button('Krunker',key='krunker', tooltip='CSGO онлайн без регистрации и смс'),sg.Button('Stick Fight',key='stickfight',tooltip='Игра где надо фигачиться с друзьями')],
[sg.Button('ASTRONEER',key='astroneer',tooltip='Игра про космос и планеты где вам надо выживать')]]

tab_cheats_layout = [[sg.Text('Тут читы')],
[sg.Text('Читы для майна: '),sg.Button('Celestial',key='celestial',tooltip='Мой любимый чит, хорош для пвп, моя любимая функция это SuperProjective при помощи нее можно убивать игроков за 1 выстрел')],
[sg.Text('Читы для CSS V34: '),sg.Button('Ultra@Hook', key='ultrahook',tooltip='Один из лучших читов для css пользовался им в 2018 2019')]]



layout = [[
[sg.Text('Привет это официальное приложение команды'),sg.Text('Dead Core',key='site',text_color='#A865C9',enable_events=True),sg.Text('кликни на текст',text_color='#453f3d'),sg.Button('Музыка', key='music')],
[sg.Text('Тут ты найдешь всякие проги, читы для игр, и т.д \nТакже вы можете навестить на кнопку программы и посмотреть описание')],
sg.TabGroup([[
    sg.Tab('Проги', tab_app_layout),
    sg.Tab('Игры', tab_games_layout),
    sg.Tab('Читы', tab_cheats_layout)]],tab_location='top', selected_title_color='purple')],
[sg.Button('Выйти',key='exit')],
[sg.Text('By Purpl3',text_color='#2a2727', enable_events=True,key='purple')]]