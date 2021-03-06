import pygame, sys
SIZE = (600,560)
screen = pygame.Surface((600,560))
window = pygame.display.set_mode(SIZE)
class Menu:
	def __init__ (self, punkts = [600, 560, u'Punkts', (26,219,30), (26,52,219)]):
		self.punkts = punkts

	def render(self, poverhnost, font, num_punkt):
		for i in self.punkts:
			if num_punkt == i[5]:
				poverhnost.blit(font.render(i[2], 1 , i[4]), (i[0], i[1]))
			else:
				poverhnost.blit(font.render(i[2], 1 , i[3]), (i[0], i[1]))
	def menu(self):
		done = True
		font_menu = pygame.font.SysFont("Ubuntu-C", 50)
		punkt = 0
		while done:
			
			screen = pygame.image.load("mainmenu.png")

			mp = pygame.mouse.get_pos()
			for i in self.punkts:
				if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
					punkt = i[5]
			self.render(screen, font_menu, punkt)

			for c in pygame.event.get():
				if c.type == pygame.QUIT:
					sys.exit()
				if c.type == pygame.KEYDOWN:
					if c.key == pygame.K_ESCAPE:
						sys.exit()

					if c.key == pygame.K_UP:
						if punkt > 0:
							punkt -= 1
					if c.key == pygame.K_DOWN:
						if punkt < len(self.punkts)-1:
							punkt += 1
					if c.key == pygame.K_SPACE:
						if punkt == 0:
							done = False
						elif punkt == 1:
							sys.exit()


			window.blit(screen, (0,0))
			pygame.display.flip()
pygame.font.init()

