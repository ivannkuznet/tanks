import pygame
from pygame import *
from pygame.sprite import Sprite, collide_rect
from pygame.image import load




bull = pygame.image.load("bullet.png")

class Bullet(sprite.Sprite):


	def __init__(self, xpos ,ypos):
		super().__init__()

		self.xvel = 0
		self.yvel = 0
		self.x = xpos
		self.y = ypos
		self.image = Surface((10,10))
		self.rect = Rect(xpos, ypos, 10, 10)
		self.image = bull

		self.rect.x += self.xvel
		self.rect.y += self.yvel
		
	def update(self, bullet, walls):


		'''if bullet.y < 0:
			bullet.push = False

		if bullet.x > 60:
			bullet.push = False'''

		if bullet.push == False:
			bullet.y = 350
			bullet.x = -10
		else:
			bullet.y -= 4
			bullet.x -= 4
		
		self.rect.x += self.xvel # переносим свои положение на xvel

		self.rect.y += self.yvel
		return self.collide(walls)


	def collide(self, walls): #столкновение со стенками
		for wl in walls:
			if collide_rect(self, wl):
				return True
				'''if self.xvel > 0:
					self.rect.right = wl.rect.left
					
					
				if self.xvel < 0:
					self.rect.left = wl.rect.right
					
				if self.yvel > 0:
					self.rect.bottom = wl.rect.top
					
				if self.yvel < 0:
					self.rect.top = wl.rect.bottom'''
		return False
			

		

