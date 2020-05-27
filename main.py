import pygame
import random
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invadors")
#icon=pygame.image.load('name')
#pygame.display.set_icon(icon)
p = pygame.image.load('player.png')
b = pygame.image.load('background.jpg')
mixer.music.load('background.wav')
mixer.music.play(-1)
playerx = 370
playery = 480
change=0
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
game_over = pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score = font.render("Score :" +str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def gameover():
    s = game_over.render("GAME OVER",True,(255,255,255))
    screen.blit(s,(200,250))
e=[]
enemyx=[]
enemyy=[]
echangex=[]
echangey=[]
numofenimies=6
for i in range(numofenimies):
    e.append(pygame.image.load('space-invaders.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    echangex.append(3)
    echangey.append(40)
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletcngx=0
bulletcngy=10
bulletstate = "ready"
def player(x,y):
    screen.blit(p,(x,y))
def enemy(x,y,i):
    screen.blit(e[i],(x,y))
def bulletfire(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt((math.pow((enemyx-bulletx),2))+math.pow((enemyy-bullety),2))
    if distance<27:
        return True
    else:
        return False
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(b,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                change = -4
            if event.key==pygame.K_RIGHT:
                change = 4
            if event.key==pygame.K_SPACE:
                if bulletstate=="ready":
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletx = playerx
                    bulletfire(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                change=0
    if bullety<=0:
        bullety=480
        bulletstate="ready"
    if bulletstate == "fire":
        bulletfire(bulletx,bullety)
        bullety = bullety-bulletcngy
    playerx = playerx+change
    if playerx<=0:
        playerx=0
    elif playerx>736:
        playerx=736
    for i in range(numofenimies):
        if enemyy[i]>440:
            for j in range(numofenimies):
                enemyy[j]=2000
            gameover()
            break
        if enemyx[i]<=0:
            echangex[i]=3
            enemyy[i] = enemyy[i] + echangey[i]
        elif enemyx[i]>736:
            echangex[i]=-3
            enemyy[i] = enemyy[i] + echangey[i]
        if iscollision(enemyx[i], enemyy[i], bulletx, bullety):
            coll_sound = mixer.Sound('explosion.wav')
            coll_sound.play()
            bullety = 480
            bulletstate = "ready"
            score_value = score_value + 1
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
        enemyx[i] = enemyx[i] + echangex[i]
        enemy(enemyx[i], enemyy[i], i)
    player(playerx,playery)
    show_score(textX,textY)
    pygame.display.update()