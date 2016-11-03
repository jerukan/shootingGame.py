import pygame, Enemy
from pygame.locals import *

class Projectile:

	PROJECTILESPEED = 11

	def __init__(s, direction, center):
		s.direction = direction
		s.model = pygame.Rect((center), (10, 10))

	def move(s):
		if s.direction == 'up':
			s.model.top -= s.PROJECTILESPEED
		if s.direction == 'down':
			s.model.top += s.PROJECTILESPEED
		if s.direction == 'right':
			s.model.right += s.PROJECTILESPEED
		if s.direction == 'left':
			s.model.right -= s.PROJECTILESPEED