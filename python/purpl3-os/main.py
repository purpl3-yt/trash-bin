import pygame
import pygame.gfxdraw
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
buttons = pygame.sprite.Group()
pygame.display.set_caption('Bios')
class Button(pygame.sprite.Sprite):
    
    def __init__(self, position, text, size,
        colors="white on blue",
        hover_colors="red on green",
        style=1,
        borderc=(255,255,255),
        command=lambda: print("Нету команды под эту кнопку")):

        super().__init__()


        self.text = text
        self.command = command
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")

        if hover_colors == "red on green":
            self.hover_colors = f"{self.bg} on {self.fg}"
        else:
            self.hover_colors = hover_colors

        self.style = style
        self.borderc = borderc
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        buttons.add(self)

    def render(self):
        self.text_render = self.font.render(self.text, 1, self.fg)
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        if self.style == 1:
            self.draw_button1()
        elif self.style == 2:
            self.draw_button2()
        if self.command != None:
            self.hover()
            self.click()

    def draw_button1(self):
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  

    def draw_button2(self):
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        pygame.gfxdraw.rectangle(screen, (self.x, self.y, self.w , self.h), self.borderc)

    def check_collision(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colors = self.hover_colors
        else:
            self.colors = self.original_colors


    def hover(self):
        if self.style == 1:
            self.check_collision()
            self.render()
        else:
            self.check_collision()

    def click(self):
        ''' checks if you click on the button and makes the call to the action just one time'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1




def on_click():
    print("Click on one answer")

def on_save():
    print("This is Save")

def on_right():
    import load

def on_false():
    quit()

def buttons_def():
    b0 = Button((150, 10), "Главное меню (Bios)", 55, "white on black",
        hover_colors="blue on orange", style=2, borderc=(0,0,0),
        command=None)

    b1 = Button((180, 200), "Начать", 36, "black on white",
        hover_colors="blue on orange", style=2, borderc=(0,0,0),
        command=on_right)

    b2 = Button((500, 200), "Выйти", 36, "black on white",
        hover_colors="blue on orange", style=2, borderc=(0,0,0),
        command=on_false)


if __name__ == '__main__':
    pygame.init()
    game_on = 0
    def loop():
        game_on = 1
        buttons_def()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    game_on = 0
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        game_on = 0
            if game_on:
                buttons.update()
                buttons.draw(screen)
            else:
                pygame.quit()
                sys.exit()
            buttons.draw(screen)
            clock.tick(60)
            pygame.display.update()
        pygame.quit()




    loop()