'''

	This template is from http://programarcadegames.com/


'''

import pygame
import math

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

COLOR_FACE = (255, 209 ,164)
COLOR_NOSE = (255, 45, 45)
COLOR_CHEEK = (255, 128 ,0)
COLOR_MOUTH = (255, 100 ,100)

pos_face_x = 0
pos_face_y = 0
vol_face_x = 0
vol_face_y = 0

size_anpanman_face = (200, 170)

size_double_jaw = (432, 768)

def Draw_Anpanman(screen, pos, level_frown) :

	# Face
	pygame.draw.ellipse(screen, COLOR_FACE, [pos[0], pos[1], size_anpanman_face[0], size_anpanman_face[1]], 0)

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

pygame.init()

scrsize = (size_double_jaw)
screen = pygame.display.set_mode(scrsize)

pygame.display.set_caption("Sosogame")

is_game_done = False
is_win = False

clock = pygame.time.Clock()

music = pygame.mixer.music.load("anpanman.ogg")
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT)

background_image = pygame.image.load("傳恩雙下巴.jpg").convert()


while not is_game_done :

	for event in pygame.event.get() :

		if event.type == pygame.QUIT :
			is_game_done = True

		elif event.type == pygame.USEREVENT :
			is_game_done = True
			is_win = True

		elif event.type == pygame.KEYDOWN :
			if event.key == pygame.K_UP :
				vol_face_y = -1
			elif event.key == pygame.K_DOWN :
				vol_face_y = 1
			elif event.key == pygame.K_LEFT :
				vol_face_x = -1
			elif event.key == pygame.K_RIGHT :
				vol_face_x = 1

	pos_face_x += vol_face_x
	pos_face_y += vol_face_y

	if pos_face_x < 0 :
		pos_face_x = 0
	if pos_face_x + size_anpanman_face[0] > size_double_jaw[0] :
		pos_face_x = size_double_jaw[0] - size_anpanman_face[0]

	if pos_face_y < 0 :
		pos_face_y = 0
	if pos_face_y + size_anpanman_face[1] > size_double_jaw[1] :
		pos_face_y = size_double_jaw[1] - size_anpanman_face[1]
		
	if pos_face_x > 30 and pos_face_x < 140 and pos_face_y > 280 and pos_face_y < 420 :
		pygame.mixer.music.unpause()
	else :
		pygame.mixer.music.pause()

	print(pos_face_x, pos_face_y)

	screen.blit(background_image, [0, 0])

	Draw_Anpanman(screen, (pos_face_x, pos_face_y), 0)

	

	pygame.display.flip()

	clock.tick(100)


level_frown = 0

while is_win :

	screen.fill(COLOR_WHITE)

	Draw_Anpanman(screen, (0, 0), level_frown)

	level_frown -= 1

	if level_frown < -20 :
		is_win = False

	pygame.display.flip()

	clock.tick(10)

pygame.time.delay(5000)

pygame.quit()