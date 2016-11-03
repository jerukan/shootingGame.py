import pygame
from Projectile import Projectile
from pygame.locals import *

class Player:

	playerModel = pygame.Rect(0, 0, 50, 50)

	MOVESPEED = 5

	shot = False
	projectiles = []

	projectileDirection = 'up'

	moveLeft = False
	moveRight = False
	moveUp = False
	moveDown = False

	def __init__(s): ()

	def shoot(s, windowWidth, windowHeight):
		if s.shot:
			s.shot = False
			s.projectiles.append(Projectile(s.projectileDirection, s.playerModel.center))

	def checkProjectileCollision(s, enemies, windowWidth, windowHeight):
		for proj in s.projectiles[:]:

			if proj.model.top < 0 or proj.model.bottom > windowHeight or proj.model.left < 0 or proj.model.right > windowWidth:
				s.projectiles.remove(proj)

			for enemy in enemies[:]:
				if proj.model.colliderect(enemy.model):
					enemies.remove(enemy)

			proj.move()

	def getInput(s, event):
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				s.moveRight = False
				s.moveLeft = True
				s.projectileDirection = 'left'
			if event.key == K_RIGHT:
				s.moveRight = True
				s.moveLeft = False
				s.projectileDirection = 'right'
			if event.key == K_UP:
				s.moveUp = True
				s.moveDown = False
				s.projectileDirection = 'up'
			if event.key == K_DOWN:
				s.moveUp = False
				s.moveDown = True
				s.projectileDirection = 'down'
			if event.key == K_SPACE:
				s.shot = True

		if event.type == KEYUP:
			if event.key == K_LEFT:
				s.moveLeft = False
			if event.key == K_RIGHT:
				s.moveRight = False
			if event.key == K_UP:
				s.moveUp = False
			if event.key == K_DOWN:
				s.moveDown = False
			if event.key == K_SPACE:
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










