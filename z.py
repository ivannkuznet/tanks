import pygame, random
from bullet import Bullet
from pygame import *
from pygame.sprite import Sprite, collide_rect
MOVE_SPEED = 1
WIDTH = 39
HEIGHT = 39
COLOR =  "#00FF00"

class Player(sprite.Sprite):
 
    def __init__(self, x, y, number):
        # sprite.Sprite.__init__(self)
        super().__init__()
        if (number == 0):
            pref = ""
        else:
            pref = "e"
        self.img = pygame.image.load(pref + "tank.png")
        self.imgrigth = pygame.image.load(pref + "tankright.png")
        self.imgleft = pygame.image.load(pref + "tankleft.png")
        self.imgdown = pygame.image.load(pref + "tankdown.png")
        self.health = 100
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.yvel = 0
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        if (number == 0):
            self.image = self.imgdown
        else:
            self.image = self.img
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        if (number == 0):
            self.direction = "down"
        else:
            self.direction = "up"


    def update(self, up, down, left, right, walls):
        

        if up:
            self.yvel = -MOVE_SPEED #вверх
            self.image = self.img
            self.direction = "up"
            
        if down:
            self.yvel = MOVE_SPEED # вниз
            self.image = self.imgdown
            self.direction = "down"

        if left:
            self.xvel = -MOVE_SPEED # Лево = x- n
            self.image = self.imgleft
            self.direction = "left"
 
        if right:
            self.xvel = MOVE_SPEED # Право = x + n
            self.image = self.imgrigth
            self.direction = "right"
            
        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0

        if not(up or down): # cтоим пока нет указаний идти
            self.yvel = 0

        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, walls)
        self.rect.y += self.yvel
        self.collide(0, self.yvel, walls)
        

    def direct(self):
        return self.direction

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
                if isinstance(wl,Bullet):
                    self.die





        





    

