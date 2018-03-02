import pygame

WHITE = (255, 255, 255)

class Block(pygame.sprite.Sprite) :

	def __init__(self, fname, scrsize):

		super().__init__()

		''' Load image as target. '''
		self.image = pygame.image.load(fname).convert()

		self.image.set_colorkey(WHITE)

		self.rect = self.image.get_rect()

		self.scrsize = scrsize