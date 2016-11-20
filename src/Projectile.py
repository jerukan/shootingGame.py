import pygame, Enemy
from pygame.locals import *

class Projectile:

	PROJECTILESPEED = 8

	def __init__(s, xSpeed, ySpeed, center):
		s.xSpeed = xSpeed
		s.ySpeed = ySpeed
		s.model = pygame.Rect((center), (10, 10))

	def move(s):
		s.model.centerx += s.xSpeed
		s.model.centery += s.ySpeed