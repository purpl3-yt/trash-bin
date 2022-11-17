from layouts import tab_app_layout,tab_cheats_layout,tab_games_layout,tab_cheats_minecraft_layout,layout
from threading import Thread
from time import sleep as delay
from txt import steps
import webbrowser
import PySimpleGUI as sg
import configparser
import pygame
import os
apps = {
#Games
'jseb': 'https://store.steampowered.com/app/531510/Just_Shapes__Beats',
'thelongdark': 'https://store.steampowered.com/app/305620/The_Long_Dark/',
'krunker': 'https://krunker.io',
'stickfight': 'https://store.steampowered.com/app/674940/Stick_Fight_The_Game/',
'astroneer': 'https://store.steampowered.com/app/361420/ASTRONEER/',
#Programs
'flameshot': 'https://flameshot.org/',
'kdeconnect': 'https://kdeconnect.kde.org/',
'kdenlive': 'https://kdenlive.org/en/',
'picasa': 'https://picasa.ru.uptodown.com/windows',
'atom': 'https://atom.io/',
'blender': 'https://www.blender.org/',
'photopea': 'https://www.photopea.com',
'bleach': 'https://www.bleachbit.org/',
'quickcpu': 'https://coderbag.com/assets/downloads/cpm/currentversion/QuickCpuSetup64.zip',
#Cheats
'celestial': 'https://drive.google.com/file/d/1CZf3vBHeRTNrXzdoJK8R5UmSHsBfYu02/view?usp=sharing',
'ultrahook': 'https://oxy.cloud/ru/d/OKlb'
}
window = sg.Window(' ', layout,finalize=True,icon='./deadcorelogo.ico',size=(680,280),resizable=False)
config = configparser.ConfigParser()
if not os.path.isfile('settings.ini'):
    with open('settings.ini','w') as cfg:
        cfg.write('''
[SETTINGS]
music = 1''')
config.read('settings.ini')
pygame.init()
play = False
if config['SETTINGS']['music']=='1':
    music = pygame.mixer.Sound('music.mp3')
    music.play()
    play = True
    window['music'].update('Музыка вкл')
elif config['SETTINGS']['music']=='0':
    music = pygame.mixer.Sound('music.mp3')
    window['music'].update('Музыка выкл')
    pass

def popup(message):
    layout = [
        [sg.Text(message)],
        [sg.Push(), sg.Button('OK')],
    ]
    sg.Window('PopUp', layout, modal=True).read(close=True)

do_text_shif = False

class ChangeTitle(Thread):
    def run(self):
        for i in range(0,len(steps)):
            delay(0.05)
            window.TKroot.title(steps[i])
class ChangeText(Thread):
    global do_text_shif
    def run(self):
        colors = ['#a865c9','#a36bcb','#9e70cc','#9a76ce','#947bcf','#8f80d1','#8a84d2','#8489d4','#7e8dd5','#7792d7','#7196d8','#6a9ada','#629edb','#5aa2dc','#51a5de','#46a9df','#3aace1','#2bb0e2']
        colors_rev = colors[::-1]
        for i in colors_rev:
            colors.append(i)
        while True:
            for x in colors:
                delay(0.2)
                window['site'].update(text_color=x)


title = ChangeTitle()
title.start()

text = ChangeText()
text.start()

while True:
    window,event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'exit':  
        break
    def check_buttons():
        global music
        global play
        global event
        #Text and etc
        if event == 'site':
            popup('Сайт уже не работает :(')
        #Games
        if event == 'jseb':
            webbrowser.open(apps['jseb'])
        elif event == 'thelongdark':
            webbrowser.open(apps['thelongdark'])
        elif event == 'krunker':
            webbrowser.open(apps['krunker'])
        elif event == 'stickfight':
            webbrowser.open(apps['stickfight'])
        elif event == 'astroneer':
            webbrowser.open(apps['astroneer'])
        #Proggrams
        elif event == 'flameshot':
            webbrowser.open(apps['flameshot'])
        elif event == 'kdeconnect':
            webbrowser.open(apps['kdeconnect'])
        elif event == 'kdenlive':
            webbrowser.open(apps['kdenlive'])
        elif event == 'picasa':
            webbrowser.open(apps['picasa'])
        elif event == 'atom':
            webbrowser.open(apps['atom'])
        elif event == 'blender':
            webbrowser.open(apps['blender'])
        elif event == 'photopea':
            webbrowser.open(apps['photopea'])
        elif event == 'bleach':
            webbrowser.open(apps['bleach'])
        elif event == 'quickcpu':
            webbrowser.open(apps['quickcpu'])
        #Cheats
        elif event == 'celestial':
            popup('В архиве будет 3 файла dll файлы надо кидать в .minecraft или .tlauncher\mcl\Minecraft\game, а папку надо в versions надеюсь ты понял')
            webbrowser.open(apps['celestial'])
        elif event == 'ultrahook':
            popup('Запустите css v34 потом uh.exe и все, если на серверах будет кикать то сделайте как тут https://www.youtube.com/watch?v=-F86mnKf-po')
            webbrowser.open(apps['ultrahook'])
        # Настройки
        elif event == 'music':
            if config['SETTINGS']['music']=='1':
                if play==False:
                    music = pygame.mixer.Sound('music.mp3')
                    music.play()
                    window['music'].update('Музыка вкл')
                    play = True
                elif play==True:
                    music.stop()
                    window['music'].update('Музыка выкл')
                    play = False
                config.set('SETTINGS', 'music', '0')
                with open('settings.ini', 'w') as configfile:
                    config.write(configfile)
                music.stop()

            elif config['SETTINGS']['music']=='0':
                if play==True:
                    music.stop()
                    window['music'].update('Музыка вкл')
                elif play==False:
                    music = pygame.mixer.Sound('music.mp3')
                    music.play()
                    window['music'].update('Музыка вкл')
                    play = True
                config.set('SETTINGS', 'music', '1')
                with open('settings.ini', 'w') as configfile:
                    config.write(configfile)
    check_buttons()
    if event == 'purple':
        popup('Discord создателя: PLNT#5507')

window.close()