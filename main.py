import pygame
from pygame import mixer
import random

pygame.init()

# SCREEN
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shooter 2D")
windowIcon = pygame.image.load("alien.png")
pygame.display.set_icon(windowIcon)

# BACKGROUND
bg = pygame.image.load("bg.png")

# FPS
clock = pygame.time.Clock()

# PLAYER
player = pygame.image.load("player.png")
playerRect = player.get_rect()
posX = 350
posY = 480
playerSpeed = 5

# LASER
laser = pygame.image.load("laser.png")
laserRect = laser.get_rect()
posLaserX = 0
posLaserY = - 100
laserSpeed = 9
canShoot = True

# SCORE
score = 0
font = pygame.font.Font("future.ttf", 36)
posTxt = 10

# MUSIC
mixer.music.load("SpaceMusic.mp3")
mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

# UFOS
ufo = []
ufoRect = []
posUfoX = []
posUfoY = []
ufoSpeed = []
nbUfo = 6


for i in range(nbUfo):
    ufo.append(pygame.image.load("ufo.png"))
    ufoRect.append(ufo[i].get_rect())
    posUfoX.append(random.randint(1, 750))
    posUfoY.append(random.randint(0, 300))
    ufoSpeed.append(3)


# COLLISION
def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # B à gauche
        return False
    if rectB.bottom < rectA.top:
        # B au-dessus
        return False
    if rectB.left > rectA.right:
        # B à droite
        return False
    if rectB.top > rectA.bottom:
        # B en-dessous
        return False
    # Ds tout les autres cas y a collision
    return True


# VARIABLE DE LA GAME LOOP
running = True

# GAME LOOP
while running:
    window.fill((0, 0, 0))
    # BACKGROUND
    window.blit(bg, (0, 0))

    for event in pygame.event.get():

        pressed = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and canShoot:
                laserSfx = mixer.Sound("sfx_laser.ogg")
                laserSfx.play()
                laserSfx.set_volume(0.9)
                canShoot = False
                posLaserX = posX + 45
                posLaserY = posY - 50

    if pressed[pygame.K_LEFT] and posX > 0:
        posX -= playerSpeed
    if pressed[pygame.K_RIGHT] and posX < 700:
        posX += playerSpeed

    # PLAYER
    playerRect.topleft = (posX, posY)
    window.blit(player, playerRect)
    # LASER
    posLaserY -= laserSpeed
    laserRect.topleft = (posLaserX, posLaserY)
    window.blit(laser, laserRect)
    if posLaserY < -40:
        canShoot = True

    # UFOS
    for i in range(nbUfo):
        posUfoX[i] -= ufoSpeed[i]
        ufoRect[i].topleft = (posUfoX[i], posUfoY[i])
        window.blit(ufo[i], ufoRect[i])
        if posUfoX[i] < 0 or posUfoX[i] > 750:
            ufoSpeed[i] = - ufoSpeed[i]
            posUfoY[i] += 50

        # COLLISION
        if collision(laserRect, ufoRect[i]):
            posUfoY[i] = 10000
            posLaserY = - 100
            score += 1
            scoreSfx = mixer.Sound("sfx_hit.ogg")
            scoreSfx.play()
            scoreSfx.set_volume(0.5)

        if collision(ufoRect[i], playerRect):
            gOSfx = mixer.Sound("foom_0.wav")
            gOSfx.play()
            gOSfx.set_volume(0.9)
            posY = - 500


    # SCORE
    scoreTxt = font.render("Score : " + str(score), True, (255, 255, 255))
    window.blit(scoreTxt, (posTxt, posTxt))

    # UPDATE
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
