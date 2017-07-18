import pygame
from gameover import Game_over
from bullet import Bullet
from z import Player
from wall import walll
from menu import Menu
from pygame import *
SIZE = (600, 560)


def Intersect(x1, x2, y1, y2, db1, db2):
    if (x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1<y2+db2):
        return 1
    else:
        return 0


white = (255,255,255)
smallfont = pygame.font.SysFont("comicsansms",25)
window = pygame.display.set_mode(SIZE)
screen = pygame.Surface((SIZE))
pygame.display.set_caption("TANK WAR")
punkts = [(100,250, u'PRESS SPACE TO START', (26,219,30), (219,65,26), 0), (260,310,u'Quit', (26,219,30), (219,65,26), 1)]
gpunkts = [(100,250, u'GAME OVER, PRESS ESC', (26,219,30), (219,65,26), 0)]

game_over = Game_over(gpunkts)


game = Menu(punkts)
game.menu()


enemy = Player(281,80, 1)
hero = Player(281,362, 0) # создаем героя по (x,y) координатам
bullet = Bullet(-10,350)
ebullet = Bullet(-20,350)
bullet.push = False
ebullet.push = False

direction = None
direction1 = None
left = right = False
up = down = False
eleft = eright = False
eup = edown = False

count = 0
count1 = 0

level =[

'---------------',
'-             -',
'- - - - - - - -',
'- - - --- - - -',
'- - -     - - -',
'- - -- - -- - -',
'-      -      -',
'-- --     -- --',
'-     ---     -',
'- - - - - - - -',
'- - -     - - -',
'- - - --- - - -',
'-             -',
'---------------',]
    

sprite_group = pygame.sprite.Group()
sprite_group.add(hero, enemy)
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
        if count >= 21 or count1 >= 21:
            done = game_over.gameover()
            #done = False


        if e.type == pygame.QUIT:
         
            done = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                game.menu()

            if e.key == pygame.K_LEFT:
                left = True
                direction = "left"
            if e.key == pygame.K_RIGHT:
                right = True
                direction = "right"
            if e.key == pygame.K_UP:
                up = True
                direction = "up"
            if e.key == pygame.K_DOWN:
                down = True
                direction = "down"   
            ''' запуск пули'''

            if e.key == pygame.K_RCTRL:

                if bullet.push == False:
                    sprite_group.add(bullet)
                    if hero.direct() == "up":
                        #direction == up
                        bullet.rect.y = hero.rect.y
                        bullet.rect.x = hero.rect.x+16
                        bullet.yvel = -5
                        bullet.xvel = 0
                        bullet.push = True
                    #if direction == down:
                    if hero.direct() == "down":
                        bullet.rect.y = hero.rect.y+39
                        bullet.rect.x = hero.rect.x+16
                        bullet.yvel = 5
                        bullet.xvel = 0
                        bullet.push = True
                    if hero.direct() == "left":
                        bullet.rect.y = hero.rect.y+16
                        bullet.rect.x = hero.rect.x
                        bullet.yvel = 0
                        bullet.xvel = -5
                        bullet.push = True
                    if hero.direct() == "right":
                        bullet.rect.y = hero.rect.y+16
                        bullet.rect.x = hero.rect.x+39
                        bullet.yvel = 0
                        bullet.xvel = 5
                        bullet.push = True
        


        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT:
                right = False
            if e.key == pygame.K_LEFT:
                left = False
            if e.key == pygame.K_UP:
                up = False
            if e.key == pygame.K_DOWN:
                down = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                eup = True
            if e.key == pygame.K_s:
                edown = True
            if e.key == pygame.K_a:
                eleft = True
            if e.key == pygame.K_d:
                eright = True

            if e.key == pygame.K_SPACE:
                if ebullet.push == False:
                    sprite_group.add(ebullet)
                    
                    if enemy.direct() == "up":
                        #direction == up
                        ebullet.rect.y = enemy.rect.y
                        ebullet.rect.x = enemy.rect.x+16
                        ebullet.yvel = -5
                        ebullet.xvel = 0
                        ebullet.push = True
                    #if direction == down:
                    if enemy.direct() == "down":
                        ebullet.rect.y = enemy.rect.y+39
                        ebullet.rect.x = enemy.rect.x+16
                        ebullet.yvel = 5
                        ebullet.xvel = 0
                        ebullet.push = True
                    if enemy.direct() == "left":
                        ebullet.rect.y = enemy.rect.y+16
                        ebullet.rect.x = enemy.rect.x
                        ebullet.yvel = 0
                        ebullet.xvel = -5
                        ebullet.push = True
                    if enemy.direct() == "right":
                        ebullet.rect.y = enemy.rect.y+16
                        ebullet.rect.x = enemy.rect.x+39
                        ebullet.yvel = 0
                        ebullet.xvel = 5
                        ebullet.push = True


        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                eup = False
            if e.key == pygame.K_s:
                edown = False
            if e.key == pygame.K_a:
                eleft = False
            if e.key == pygame.K_d:
                eright = False



    if (bullet.update(bullet, walls)):
        sprite_group.remove(bullet)
        bullet.push = False
    if (ebullet.update(ebullet, walls)):
        sprite_group.remove(ebullet)
        ebullet.push = False





    screen.fill((161, 141, 75))

    if Intersect(bullet.rect.x, enemy.rect.x, bullet.rect.y, enemy.rect.y, 10, 40) == True:
        bullet.push = False
        sprite_group.remove(bullet)
        count += 0.1

    if Intersect(ebullet.rect.x, hero.rect.x, ebullet.rect.y, hero.rect.y, 10, 40) == True:
        ebullet.push = False
        sprite_group.remove(ebullet)
        count1 += 0.1

    hero.update(up, down, left, right, walls) # передвижение
    enemy.update(eup, edown, eleft, eright, walls)
    
    if count == 3:
        gameover = True


    sprite_group.draw(screen)

    window.blit(screen, (0,0))

    text = smallfont.render("Score green: " + str(int(count)) + "    " + "Score blue: " + str(int(count1)), True, white)
    window.blit(text, [0,0])

    pygame.display.flip()
    timer.tick(60)

