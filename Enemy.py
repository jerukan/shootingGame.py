import pygame
from pygame.locals import *

class Enemy:

	def __init__(s, left, top):
		s.model = pygame.Rect(left, top, 40, 40)
