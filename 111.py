import pygame
from z import Player
from wall import walll
SIZE = (600, 560)

window = pygame.display.set_mode(SIZE)
screen = pygame.Surface((SIZE))
pygame.display.set_caption("WORLD OF TANKS 2D VERSION")

hero = Player(281,362) # создаем героя по (x,y) координатам
left = right = False
up = down = False

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
    

sprite_group = pygame.sprite.Group()
sprite_group.add(hero)
walls = []
#wl = walll()
x = 0
y = 0
for row in level:
    for cor in row:
        if cor == "-":
            wl = walll(x,y)
            sprite_group.add(wl)
            walls.append(wl)
        x+=40
    y+=40
    x = 0


done = True
timer = pygame.time.Clock()
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

    hero.update(up, down, left, right, walls) # передвижение
    #hero.draw(screen) # отображение
    sprite_group.draw(screen)

    window.blit(screen, (0,0))

    pygame.display.flip()
    timer.tick(60)

