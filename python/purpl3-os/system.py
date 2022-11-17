import pygame as pg #Импорт
import sys #Импорт
import webbrowser #Импорт
from time import sleep as wait #Импорт
import time
from playsound import playsound #Импорт
import configparser #Импорт

config = configparser.ConfigParser()#Конфиг с темами ит.д

FPS = 60#Кадры в сек
pg.init()#хз просто надо
sc = pg.display.set_mode((800, 600))#Разрешение
pg.display.set_caption('Purpl3 OS on Pygame')#Название окна OS
clock = pg.time.Clock()#Кадры в секунду
pg.display.update()#обновление экрана


show_menu = False#Статус меню
show_amogus = False#Статус амогуса
show_themes = False#Статус тем
show_browser = False#Статус браузера
show_easter_egg = False#Статус пасхалки

config.read('settings.ini')
if str(config.get('DEFAULT', 'theme'))=='white':#если в файле settings.ini переменная theme есть white то сделать белую тему
    theme_r = 255# Красный
    theme_g = 255# Синий
    theme_b = 255# Зелёный
elif str(config.get('DEFAULT', 'theme'))=='purple':#то что также но с фиолетовой темой
    theme_r = 138# Красный
    theme_b = 43# Синий
    theme_g = 226# Зелёный

font = pg.font.SysFont(None, 30)#Шрифт и размер
text = "Пишите сюда"#Текст
input_active = True#Статус режима писания

#--------------Функции-----------
def image(source_image,transform_x,transform_y,pos_x,pos_y):#Пресет для вывода картинок (для удобства)
    picture = pg.image.load(source_image)
    picture_scale = pg.transform.scale(picture, (transform_x,transform_y))
    picture_scale_rect = picture_scale.get_rect(center=(pos_x,pos_y))
    sc.blit(picture_scale,picture_scale_rect)
 
def base():#База приложений (для удобсва)
    pg.draw.rect(sc, (255, 255, 255), (300,100,300,400))#база для приложений
    pg.draw.rect(sc, (255,0,0), (550,100,50,50))#Кнопка закрыть
    pg.draw.line(sc,(255,255,255),(550,100),(600,150),3)#Крест для кнопки закрыть
    pg.draw.line(sc,(255,255,255),(600,100),(550,150),3)#Крест для кнопки закрыть

def print_text(text,x,y,scale,color_r,color_g,color_b):#Пресет текстов ну типо того (для удобства)
        f1 = pg.font.Font(None, scale)
        text1 = f1.render(text, True,(color_r, color_g, color_b))
        sc.blit(text1, (x, y))
while True:
    clock.tick(FPS)#Кадры в секунду
    sc.fill((0,0,0))#Задний фон но его закрывает след. строка
    keys = pg.key.get_pressed()
    image('wallpaper.jpg',800,600,400,300)
        
    print_text('Purpl3 OS',700,10,30,255,255,255)#пасхалка
    
    pg.draw.rect(sc, (theme_r, theme_b,theme_g), (0, 550, 800, 50))#панель
    
    if show_menu==True:#Показывать меню приложений
        pg.draw.rect(sc, (theme_r, theme_b,theme_g), (0, 250, 200, 300))#меню приложений
        print_text('Создатель',50,260,30,0,0,0)#октрывает ссыллку в браузере на тик ток создателя
        pg.draw.rect(sc, (0,0,0), (0,250,200,40),2)#Рамка приложения

        print_text('Не нажимать!!!',30,300,30,0,0,0)#пасхалка
        pg.draw.rect(sc, (0,0,0), (0,290,200,40),2)#Рамка приложения

        print_text('Темы',65,340,30,0,0,0)#октрывает меню тем
        pg.draw.rect(sc, (0,0,0), (0,330,200,40),2)#Рамка приложения

        print_text('Браузер',50,380,30,0,0,0)#октрывает меню браузера
        pg.draw.rect(sc, (0,0,0), (0,370,200,40),2)#Рамка приложения

        #print_text('Игра',70,420,30,0,0,0)#игры не будет :( 
        #pg.draw.rect(sc, (0,0,0), (0,410,200,40),2)#Рамка приложения

    if show_amogus==True:#Показывать приложение амогуса
        show_menu=False#Скрывать меню
        base()#База для приложений
        image('amogus.jpg',250,250,450,300)

    if show_themes==True:
        show_menu=False
        base()
        pg.draw.rect(sc,(0,0,0), (300,100,250,120),2)#Рамка purple темы
        pg.draw.circle(sc,(138,43,226),(410,150),30)#Purple Тема
        print_text('Purple',380,190,30,0,0,0)#выбор темы

        pg.draw.rect(sc,(0,0,0), (300,220,250,120),2)#Рамка обычной темы
        pg.draw.circle(sc,(0,0,0),(410,270),30)#Обычная тема
        print_text('Обычная тема',340,310,30,0,0,0)#выбор темы

    if show_browser==True:#Если нажать на браузер
        show_menu=False#Скрывать меню
        base()#База для приложений
        pg.draw.rect(sc,(0,0,0),(330,195,230,100),3)#Рамка для текста
        pg.draw.rect(sc,(0,0,0),(345,300,200,60),3)#Рамка для кнопки "поиск"
        print_text('Поиск',420,320,30,0,0,0)#кнопка поиска в браузере
        text_surf = font.render(text, True, (0, 0, 0))
        sc.blit(text_surf, text_surf.get_rect(center = (450,250)))

    if show_easter_egg==True:#Если нажать на пасхалку 
        show_menu=False#Скрывает меню
        base()#База для приложений
        print_text('Purpl3 OS Версии 2022 года',300,320,30,0,0,0)#пасхалка



    image('os_menu.png',60,60,30,575)#Иконка меню пуск
    image('off_icon.png',100,100,760,575)#Иконка выключения
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        

        elif event.type == pg.KEYDOWN and input_active:#Текст в браузере
            if event.key == pg.K_RETURN:
                input_active = False
            elif event.key == pg.K_BACKSPACE:#если нажат backspace удалить 1 символ из текста
                text =  text[:-1]
            else:
                text += event.unicode
        

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            
            #print(pos)
            #--------НАЖАТИЕ НА ПУСК-------
            if pos[0] in range(10,50) and pos[1] in range(551,600):#на нажатие пуск
                    show_menu=True
            
            elif pos[0] in range(200,800):
                    show_menu=False
            
            elif pos[1] in range(0,250):
                    show_menu=False

            #--------КНОПКА ВЫКЛЮЧЕНИЯ-------

            if pos[0] in range(740,800) and pos[1] in range(551,600):#При нажатии на кнопку выключения
                quit()

            #--------ПРИЛОЖЕНИЯ ИЗ МЕНЮ ПУСК-------
            

                

            if show_amogus==True or show_themes==True or show_browser==True or show_easter_egg==True:
                if pos[0] in range(550,600) and pos[1] in range(100,150):#В амогусе и темах и т.д кнопка закрыть
                    show_amogus=False
                    show_themes=False
                    show_browser=False
                    show_easter_egg=False
            
            #if show_game==True:
                #if pos[0] in range(600,650) and pos[1] in range(100,150):#Игры не будет :(
                    #show_game=False

            if show_amogus==True:
                if pos[0] in range(325,575) and pos[1] in range(175,425):#В амогусе при нажатии амогуса
                    playsound('./amogus.mp3')

            if show_menu==True:
                if pos[0] in range(0,200) and pos[1] in range(330,370):#Меню тем
                    show_themes=True

            
                if pos[0] in range(0,200) and pos[1] in range(370,410):#Браузер
                    show_browser=True

            
                if pos[0] in range(0,200) and pos[1] in range(410,450):#Мини игра
                    show_game=True

                if pos[0] in range(0,200) and pos[1] in range(290,330):#Меню амогуса
                    show_amogus=True

                if pos[0] in range(0,200) and pos[1] in range(250,290):#Ссылка на тт создателя
                    webbrowser.open('https://www.tiktok.com/@purpl3_dc')



            if show_themes==True:#Меняет тему на фиолетовою
                if pos[0] in range(300,550) and pos[1] in range(100,220):
                    config['DEFAULT'] = {'theme': 'purple'}
                    with open('settings.ini', 'w') as configfile:config.write(configfile)
                    theme_r = 138
                    theme_b = 43
                    theme_g = 226

                if pos[0] in range(300,550) and pos[1] in range(220,220+120):
                    config['DEFAULT'] = {'theme': 'white'}
                    with open('settings.ini', 'w') as configfile:config.write(configfile)
                    theme_r = 255
                    theme_b = 255
                    theme_g = 255


            if show_browser==True:#Браузер строка поиска
                if pos[0] in range(330,330+230) and pos[1] in range(195,195+100):
                    input_active = True
                    text = ''

            if show_browser==True:#Браузер кнопка поиск
                if pos[0] in range(345,345+200) and pos[1] in range(300,360):
                    input_active = False
                    webbrowser.open(f'https://www.google.com/search?&q={text}')

            if show_menu==False and show_amogus==False and show_themes==False and show_browser==False:
                if pos[0] in range(695,800) and pos[1] in range(2,33):
                    show_easter_egg=True


    pg.display.update()
