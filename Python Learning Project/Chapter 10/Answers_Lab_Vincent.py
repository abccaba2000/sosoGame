import pygame
import math

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

COLOR_FACE = (255, 209 ,164)
COLOR_NOSE = (255, 45, 45)
COLOR_CHEEK = (255, 128 ,0)
COLOR_MOUTH = (255, 100 ,100)

pygame.init()
pygame.display.init()

size = [800, 600]
screen = pygame.display.set_mode(size)

level_frown = 0
level_frown_speed = 0
level_frown_upbound = -20
level_frown_lowbound = 10


def Draw_Anpanman(screen, pos, level_frown) :

	# Face
	pygame.draw.ellipse(screen, COLOR_FACE, [pos[0], pos[1], 200, 170], 0)

	# Frown

	pygame.draw.arc(screen, COLOR_BLACK, [pos[0] + 50, pos[1] + 30, 40, 50], 0, math.pi, 2)

	pygame.draw.arc(screen, COLOR_BLACK, [pos[0] + 110, pos[1] + 30 + level_frown, 40, 50], 0, math.pi, 2)

	# Eye

	pygame.draw.ellipse(screen, COLOR_BLACK, [pos[0] + 66, pos[1] + 50, 10, 20], 0)

	pygame.draw.ellipse(screen, COLOR_BLACK, [pos[0] + 125, pos[1] + 50, 10, 20], 0)

	# Cheek

	pygame.draw.ellipse(screen, COLOR_CHEEK, [pos[0] + 30, pos[1] + 80, 40, 40], 0)

	pygame.draw.ellipse(screen, COLOR_CHEEK, [pos[0] + 130, pos[1] + 80, 40, 40], 0)

	# Nose

	pygame.draw.ellipse(screen, COLOR_NOSE, [pos[0] + 70, pos[1] + 70, 60, 60], 0)

	# Mouth

	pygame.draw.arc(screen, COLOR_BLACK, [pos[0] + 62, pos[1] + 90, 80, 50], math.pi+0.3, 0-0.3, 2)


pygame.display.set_caption("Sosogame")

done = False

clock = pygame.time.Clock()

while not done :

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			done = True

		elif event.type == pygame.KEYDOWN :

			if event.key == pygame.K_UP :
				level_frown_speed = -1
			elif event.key == pygame.K_DOWN :
				level_frown_speed = 1

		elif event.type == pygame.KEYUP :
			level_frown_speed = 0

	
	level_frown += level_frown_speed

	if level_frown < level_frown_upbound :
		level_frown = level_frown_upbound

	if level_frown > level_frown_lowbound :
		level_frown = level_frown_lowbound

	pos = pygame.mouse.get_pos()

	pos = list(pos)

	if pos[0] + 200 > size[0] :
		pos[0] = size[0] - 200

	if pos[1] + 170 > size[1] :
		pos[1] = size[1] - 170


	screen.fill(COLOR_BLACK)


	Draw_Anpanman(screen, pos, level_frown)

	pygame.display.flip()

	clock.tick(100)

pygame.quit()