import pygame
from pygame import *
from pygame.sprite import Sprite, collide_rect
MOVE_SPEED = 1 
WIDTH = 39
HEIGHT = 39
COLOR =  "#00FF00"


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.yvel = 0
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image = pygame.image.load("tank.png")
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект

    def update(self, up, down, left, right, walls):
        if up:
            self.yvel = -MOVE_SPEED
        if down:
            self.yvel = MOVE_SPEED

        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
 
        if right:
            self.xvel = MOVE_SPEED # Право = x + n
         
        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        if not(up or down):
            self.yvel = 0

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, walls)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, walls)

    def collide(self, xvel, yvel, walls):
        for wl in walls:
            if collide_rect(self, wl):
                if xvel > 0:
                    self.rect.right = wl.rect.left
                if xvel < 0:
                    self.rect.left = wl.rect.right
                if yvel > 0:
                    self.rect.bottom = wl.rect.top                   
                if yvel < 0:
                    self.rect.top = wl.rect.bottom
   
    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))

    

