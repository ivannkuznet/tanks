import pygame
from z import Player

SIZE = (600, 560)

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface((SIZE))
pygame.display.set_caption("WORLD OF TANKS 2D VERSION")


class walll():
    
    def __init__(self):
        self.image = pygame.image.load("C:/Users/ivann/Python1/walll.png").convert()
        self.rect = self.image.get_rect()


def make_level(level, wall):
    x = 0
    y = 0
    for row in level:
        for cor in row:
            if cor == "-":
                #screen.blit(wall,(x,y))
                screen.blit(wl.image ,(x,y))
            x+=40
        y+=40
        x = 0

level =[

'---------------',
'-             -',
'- - - - - - - -',
'- - - - - - - -',
'- - - - - - - -',
'- - -     - - -',
'-     ---     -',
'-- --     -- --',
'-     ---     -',
'- - - - - - - -',
'- - -     - - -',
'- - - --- - - -',
'-             -',
'---------------',]
    
wl = walll()
#wl = pygame.Surface((40, 40)
#wl.fill((130, 130, 130))

hero = Player(281,362) # создаем героя по (x,y) координатам
left = right = False
up = down = False    # по умолчанию — стоим

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

        #Движение персонажа
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                left = True
            if e.key == pygame.K_RIGHT:
                right = True
            if e.key == pygame.K_UP:
                up = True

            if e.key == pygame.K_DOWN:
                down = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_UP:
                up = False

            if e.key == pygame.K_DOWN:
                down = False
            




    screen.fill((161, 141, 75))

    make_level(level, wl)

    hero.update(up, down, left, right) # передвижение
    hero.draw(screen) # отображение


    window.blit(screen, (0,0))

    pygame.display.flip()

