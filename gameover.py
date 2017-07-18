import pygame, sys

SIZE = (600,560)
screen = pygame.Surface((600,560))
window = pygame.display.set_mode(SIZE)
class Game_over:
	def __init__ (self, gpunkts = [600, 560, u'Punkts', (26,219,30), (26,52,219)]):
		self.gpunkts = gpunkts

	def render(self, poverhnost, font, num_gpunkt):
		for i in self.gpunkts:
			if num_gpunkt == i[5]:
				poverhnost.blit(font.render(i[2], 1 , i[4]), (i[0], i[1]))
			else:
				poverhnost.blit(font.render(i[2], 1 , i[3]), (i[0], i[1]))
	def gameover(self):
		game = True
		font_menu = pygame.font.SysFont("Ubuntu-C", 50)
		gpunkt = 0
		while game:
			
			screen.fill((161, 141, 75))

			mp = pygame.mouse.get_pos()
			for i in self.gpunkts:
				if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+50:
					punkt = i[5]
			self.render(screen, font_menu, gpunkt)

			for c in pygame.event.get():
				if c.type == pygame.QUIT:
					sys.exit()
				if c.type == pygame.KEYDOWN:
					if c.key == pygame.K_ESCAPE:
						sys.exit()

					if c.key == pygame.K_UP:
						if gpunkt > 0:
							gpunkt -= 1
					if c.key == pygame.K_DOWN:
						if gpunkt < len(self.gpunkts)-1:
							gpunkt += 1
					if c.key == pygame.K_SPACE:
						if gpunkt == 0:
							game = False
							

							
						elif gpunkt == 1:
							sys.exit()


			window.blit(screen, (0,0))
			pygame.display.flip()
pygame.font.init()