
from pygame.sprite import Sprite
from pygame.image import load
 
class walll(Sprite):
    def __init__(self, x, y):
    	Sprite.__init__(self)
    	self.image = load("C:/Users/ivann/Python1/walll.png").convert()
    	self.rect = self.image.get_rect()
    	self.rect.x = x
    	self.rect.y = y
    	
    	