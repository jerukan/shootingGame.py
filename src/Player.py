import pygame, math
from Projectile import Projectile
from pygame.locals import *


class Player:
    playerModel = pygame.Rect(0, 0, 50, 50)

    MOVESPEED = 5

    shot = False
    projectiles = []

    moveLeft = False
    moveRight = False
    moveUp = False
    moveDown = False

    mousePos = (0, 0)

    def __init__(s): ()

    def shoot(s):
        if s.shot:
            mousePos = pygame.mouse.get_pos()

            x = mousePos[0]
            y = mousePos[1]

            xDist = x - s.playerModel.centerx
            yDist = y - s.playerModel.centery

            if xDist == 0 or yDist == 0:
                return

            distance = math.sqrt(((xDist) ** 2) + ((yDist) ** 2))

            xSpeed = Projectile.PROJECTILESPEED * (xDist / distance)
            ySpeed = Projectile.PROJECTILESPEED * (yDist / distance)

            s.projectiles.append(Projectile(xSpeed, ySpeed, s.playerModel.center))

            # comment to make full auto
            s.shot = False

    def checkProjectileCollision(s, enemies, windowWidth, windowHeight):
        for proj in s.projectiles[:]:

            if proj.model.top < 0 or proj.model.bottom > windowHeight or proj.model.left < 0 or proj.model.right > windowWidth:
                s.projectiles.remove(proj)

            for enemy in enemies[:]:
                if proj.model.colliderect(enemy.model):
                    enemies.remove(enemy)
                    s.projectiles.remove(proj)

            proj.move()

    def getInput(s, event):
        if event.type == KEYDOWN:
            if event.key == K_a:
                s.moveRight = False
                s.moveLeft = True
            if event.key == K_d:
                s.moveRight = True
                s.moveLeft = False
            if event.key == K_w:
                s.moveUp = True
                s.moveDown = False
            if event.key == K_s:
                s.moveUp = False
                s.moveDown = True

        if event.type == KEYUP:
            if event.key == K_a:
                s.moveLeft = False
            if event.key == K_d:
                s.moveRight = False
            if event.key == K_w:
                s.moveUp = False
            if event.key == K_s:
                s.moveDown = False

        if event.type == MOUSEBUTTONDOWN:
            s.shot = True
        if event.type == MOUSEBUTTONUP:
            s.shot = False

    def movePlayer(s, windHeight, windWidth):
        model = s.playerModel
        MOVESPEED = s.MOVESPEED

        if s.moveDown and model.bottom < windHeight:
            model.top += MOVESPEED
        if s.moveUp and model.top > 0:
            model.top -= MOVESPEED
        if s.moveRight and model.right < windWidth:
            model.left += s.MOVESPEED
        if s.moveLeft and model.left > 0:
            model.left -= MOVESPEED
