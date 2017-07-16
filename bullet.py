import pygame
from pygame import *
from pygame.sprite import Sprite
from pygame.image import load

bull = pygame.image.load("bullet.png")

class Bullet(sprite.Sprite):


	def __init__(self, x ,y):
		super().__init__()

		self.xvel = 0
		self.yvel = 0
		self.x = x
		self.y = y
		self.image = Surface((20,20))
		self.rect = Rect(x, y, 10, 10)
		self.image = bull
		#self.image = load("C:/Users/ivann/Python1/bullet.png").convert()
	#def render(self):
		#screen.blit(self.image, (self.x, self.y))

	def update(self, bullet):


		if bullet.y > 600:
			bullet.push = False
		if bullet.x > 560:
			bullet.push = False
		if bullet.push == False:
			bullet.y = 352
			bullet.x = -10
		else:
			bullet.y -= 1
			bullet.x -= 1
		


		self.rect.x += self.xvel
		self.rect.y += self.yvel

