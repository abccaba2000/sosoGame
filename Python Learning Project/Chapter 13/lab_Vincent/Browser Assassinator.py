"""	DOCSTRING

	This template is retrieved from :http://programarcadegames.com/
"""

import pygame
import random


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)

pygame.init()

sound_good = pygame.mixer.Sound("good.wav")
sound_bad = pygame.mixer.Sound("bad.wav")
sound_bump = pygame.mixer.Sound("bump.wav")


class Target(pygame.sprite.Sprite) :

	def __init__(self, fname):

		super().__init__()

		''' Load image as target. '''
		self.image = pygame.image.load(fname).convert()

		self.image.set_colorkey(WHITE)

		self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite) :

	def __init__(self, fname):

		super().__init__()

		''' Load image as player. '''
		self.image = pygame.image.load(fname).convert()

		self.image.set_colorkey(WHITE)

		''' Set initial position. '''
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0

		''' Set Speed. '''
		self.change_x = 0
		self.change_y = 0


	''' Change the speed. '''
	def transmission(self, x, y):

		self.change_x += x
		self.change_y += y


	'''	Update the position of player.

		According to "pygame doc", the base Sprite class has an update method that takes any number of arguments and does nothing. We override it to update the position information of player.

		According to "pygame doc", the arguments passed to Group.update() will be passed to each Sprite.

		Ensure the player from out of screen.
	'''
	def update(self):

		self.rect.x += self.change_x
		self.rect.y += self.change_y

		if self.rect.x < 0 :
			self.rect.x = 0
			sound_bump.play()

		if self.rect.x + self.rect.width > screen_size[0] :
			self.rect.x = screen_size[0] - self.rect.width
			sound_bump.play()

		if self.rect.y < 0 :
			self.rect.y = 0
			sound_bump.play()

		if self.rect.y + self.rect.height > screen_size[1] :
			self.rect.y = screen_size[1] - self.rect.height
			sound_bump.play()


screen_size = [700, 400]
screen = pygame.display.set_mode(screen_size)

'''	Create sprite lists.

	Using sprite.Group() container.

	"list_all" includes good targets, bad targets, and player.
'''
list_good = pygame.sprite.Group()
list_bad = pygame.sprite.Group()
list_all = pygame.sprite.Group()


'''	Create target objects & Add targets to lists. '''
for new_obj in range(50) :

	obj_good = Target("Chrome.png")
	obj_bad = Target("Firefox.png")


	obj_good.rect.x = random.randrange(screen_size[0] - obj_good.rect.width)
	obj_good.rect.y = random.randrange(screen_size[1] - obj_good.rect.height)

	list_good.add(obj_good)
	list_all.add(obj_good)


	obj_bad.rect.x = random.randrange(screen_size[0] - obj_bad.rect.width)
	obj_bad.rect.y = random.randrange(screen_size[1] - obj_bad.rect.height)

	list_bad.add(obj_bad)
	list_all.add(obj_bad)


''' Create player object & Add player to list. '''
player = Player("Edge.png")
list_all.add(player)


game_done = False

clock = pygame.time.Clock()

font = pygame.font.SysFont('Calibri', 25, True, False)

score = 0


''' Instruction-Vector pairs. '''
vec_speed = { \

	pygame.K_LEFT : [-3, 0], \
	pygame.K_RIGHT : [3, 0], \
	pygame.K_UP : [0, -3], \
	pygame.K_DOWN : [0, 3] \

}


''' Game Loop. '''
while not game_done :

	for event in pygame.event.get() : 

		if event.type == pygame.QUIT : 
			game_done = True

		elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP :

			for key in [*vec_speed] :
				if key == event.key :
					vec_x, vec_y = vec_speed[key][0], vec_speed[key][1]


			if event.type == pygame.KEYDOWN :
				player.transmission(vec_x, vec_y)

			elif event.type == pygame.KEYUP :
				player.transmission(-vec_x, -vec_y)
		

	screen.fill(WHITE)

	list_hit_good = pygame.sprite.spritecollide(player, list_good, True)
	list_hit_bad = pygame.sprite.spritecollide(player, list_bad, True)

	for hit in list_hit_good :
		score += 1
		sound_good.play()

	for hit in list_hit_bad :
		score -= 1
		sound_bad.play()

	list_all.update()

	''' Show score on the screen. '''
	text = font.render(str(score), True, BLACK)
	screen.blit(text, [0, 0])

	''' Draw all the sprites on screen. '''
	list_all.draw(screen)

	pygame.display.flip()

	clock.tick(60)

pygame.quit()
