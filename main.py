import json
from pygame import *
from random import *
font.init()
FPS = 40
WIDTH = 1000
HEIGHT = 500
WIDTH_RAKET = 20
HEIGHT_RAKET = 200

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        draw.rect(window, (255,0,0), self.rect, 2)
class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= self.speed:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom <= HEIGHT - self.speed:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= self.speed:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom <= HEIGHT - self.speed:
            self.rect.y += self.speed
right_raket = Player('Raket.png', WIDTH - WIDTH_RAKET - 5, HEIGHT / 2 - HEIGHT_RAKET / 2, 5, WIDTH_RAKET, HEIGHT_RAKET)
left_raket = Player('Raket.png', 5, HEIGHT / 2 - HEIGHT_RAKET / 2, 5, WIDTH_RAKET, HEIGHT_RAKET)
bg = image.load('Table.png')
bg = transform.scale(bg, (WIDTH, HEIGHT))
clock = time.Clock()
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping Pong')
run = True
while run:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            run = False
    window.blit(bg, (0, 0))
    right_raket.update_right()
    left_raket.update_left()
    right_raket.reset()
    left_raket.reset()
    display.update()
    clock.tick(FPS)
    
