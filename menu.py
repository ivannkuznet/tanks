import pygame, sys

punkts = [(120,140, u'Game', (250,250,30), (250,30,250), 0), (130,210,u'Quit', (250,250,30), (250,30,250), 1)]
game = menu(punkts)

class menu:
	def __init__ (self, punkts = [120, 140, u'Punkts', (250,250,30), (250,30,250)]):
		self.punkts = punkts

	def render(self, poverhnost, font, num_punkt):
		for i in self.punkts:
			if num_punkt == i[5]:
				poverhnost.blit(font.render(i[2], 1 , i[4]), (i[0], i[1]))
			else:
				poverhnost.blit(font.render(i[2], 1 , i[3]), (i[0], i[1]))
	def menu(self):
		done = True
		font_menu = pygame.font.Font()
		punkt = 0
		while done:
			screen.fill((0, 100, 200))

			for c in pygame.event.get():
				if c.type == pygame.Quit:
					sys.exit()
				if c.type == pygame.KEYDOWN:
					if c.key == pygame.K_ESCAPE:
						sys.exit()
			window.blit(screen, (0,0))
			pygame.display.flip()


