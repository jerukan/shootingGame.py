import pygame, sys, Player, Projectile, Enemy, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

player = Player.Player()

enemies = []
ENEMYADDRATE = 50
enemyAddTime = 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		player.getInput(event)

	windowSurface.fill(BLACK)

	if enemyAddTime == ENEMYADDRATE:
		enemyAddTime = 0
		enemies.append(Enemy.Enemy(random.randint(0, WINDOWWIDTH - 40), random.randint(0, WINDOWHEIGHT - 40)))
	else:
		enemyAddTime += 1

	player.shoot()

	for proj in player.projectiles[:]:
		pygame.draw.rect(windowSurface, WHITE, proj.model)
		proj.move()

	for enemy in enemies[:]:
		pygame.draw.rect(windowSurface, RED, enemy.model)
	
	player.checkProjectileCollision(enemies, WINDOWHEIGHT, WINDOWWIDTH)

	player.movePlayer(WINDOWHEIGHT, WINDOWWIDTH)
	pygame.draw.rect(windowSurface, WHITE, player.playerModel)

	pygame.display.update()
	mainClock.tick(40)




