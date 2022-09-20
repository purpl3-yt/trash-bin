import pygame as pg
import sys
from time import sleep as wait
FPS = 60
pg.init()
sc = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
pg.display.update()

pg.display.set_caption('Loading OS')
bios_logo = pg.image.load('bios_logo.png')
bios_logo_scale = pg.transform.scale(bios_logo, (500, 120))
bios_logo_scale_rect = bios_logo_scale.get_rect(center=(260,75))
load = False
load1 = False
while True:
    clock.tick(FPS)
    sc.fill((0,0,0))
    if load==False:
        wait(1)
        load=True
    sc.blit(bios_logo_scale, bios_logo_scale_rect)
    def print_text(text,x,y,scale,color_r,color_g,color_b):
        f1 = pg.font.Font(None, scale)
        text1 = f1.render(text, True,(color_r, color_g, color_b))
        sc.blit(text1, (x, y))
    #            text     x   y  sc col1 col2 col3
    print_text('American',230,20,70,255,255,255)
    print_text('Megatrends',230,80,70,255,255,255)
    print_text('By Purpl3',730,10,20,255,255,255)
    print_text('www.ami.com',75,120,20,255,255,255)
    if load1==False:
        pg.display.update()
        wait(1)
        load1=True
    print_text('Speed: 3.19 GHz ',10,170,30,255,255,255)
    print_text('AMLBIOS (C) 2608 American Megatrends. Inc.',10,200,30,255,255,255)
    print_text('ASUS PSK PRO ACPI BIOS Revision 1202',10,230,30,255,255,255)
    print_text('Loading...',10,260,30,255,255,255)
    
    pg.display.update()
    wait(2)
    import system
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.display.update()