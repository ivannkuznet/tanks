import pygame, random
from bullet import Bullet
from pygame import *
from pygame.sprite import Sprite, collide_rect
MOVE_SPEED = 1 
WIDTH = 39
HEIGHT = 39
COLOR =  "#00FF00"


img = pygame.image.load("etankup.png")
imgrigth = pygame.image.load("etankright.png")
imgleft = pygame.image.load("etankleft.png")
imgdown = pygame.image.load("etankdown.png")

class Enemy(sprite.Sprite):

   
    def __init__(self, x, y):
        # sprite.Sprite.__init__(self)
        super().__init__()
        self.health = 100
        self.xvel = 1   #скорость перемещения. 0 - стоять на месте
        self.yvel = 0
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image = imgdown
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект




        '''self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, walls)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, walls)
        '''

    def collide(self, xvel, yvel, walls): #столкновение со стенками
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