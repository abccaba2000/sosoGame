import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN   = (0,   255,   0)
BLUE = (  0,   0, 255)
HEIGHT = 400
WIDTH = 700

TEXT_SIZE = 25
TEXT_POSITION = [int( WIDTH/2-TEXT_SIZE ), int( HEIGHT/3 )]

class Block(pygame.sprite.Sprite):
	"""
	This class represents the ball.
	It derives from the "Sprite" class in Pygame.
	"""
 
	def __init__(self, color, width, height):
		""" Constructor. Pass in the color of the block,
		and its x and y position. """
 
		# Call the parent class (Sprite) constructor
		super().__init__()
 
		# Create an image of the block, and fill it with a color.
		# This could also be an image loaded from the disk.
		self.height = height
		self.width = width
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
 
		# Fetch the rectangle object that has the dimensions of the image
		# image.
		# Update the position of this object by setting the values
		# of rect.x and rect.y
		self.rect = self.image.get_rect()

class Player(Block):
	""" The class is the player-controlled sprite. """
 
	# -- Methods
	def __init__(self, color, x, y, width, height):
		"""Constructor function"""
		# Call the parent's constructor
		super().__init__(color, width, height)

 
		# Make our top-left corner the passed-in location.
		self.rect.x = x
		self.rect.y = y
 
		# -- Attributes
		# Set speed vector
		self.change_x = 0
		self.change_y = 0
		self.bump_x = False
		self.bump_y = False
 
	def changespeed(self, x, y):
		""" Change the speed of the player"""
		self.change_x += x
		self.change_y += y
 
	def update(self):
		""" Find a new position for the player"""
		self.rect.x += self.change_x
		self.rect.y += self.change_y
		
		if self.rect.x <= 0:
			self.rect.x = 0
			if not self.bump_x:
				bump_sound.play()
				self.bump_x = True				
		elif self.rect.x + self.width >= WIDTH:
			self.rect.x = WIDTH - self.width
			if not self.bump_x:
				bump_sound.play()
				self.bump_x = True
		else:
			self.bump_x = False
			
		if self.rect.y <= 0:
			self.rect.y = 0
			if not self.bump_y:
				bump_sound.play()
				self.bump_y = True				
		elif self.rect.y - self.height >= HEIGHT:
			self.rect.y = HEIGHT - self.height
			if not self.bump_y:
				bump_sound.play()
				self.bump_y = True
		else:
			self.bump_y = False
			
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Collide don\'t be angry')

font = pygame.font.SysFont('Calibri', TEXT_SIZE, True, False)

bump_sound = pygame.mixer.Sound("bump.wav")
bad_sound = pygame.mixer.Sound("bad_block.wav")
good_sound = pygame.mixer.Sound("good_block.wav")

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
bad_block_list = pygame.sprite.Group()
good_block_list = pygame.sprite.Group()

# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
	# This represents a block
	good_block = Block(GREEN, 20, 15)
	bad_block = Block(RED, 20, 15)
	# Set a random location for the block
	good_block.rect.x = random.randrange(WIDTH)
	good_block.rect.y = random.randrange(HEIGHT)
	bad_block.rect.x = random.randrange(WIDTH)
	bad_block.rect.y = random.randrange(HEIGHT)
	
	# Add the block to the list of objects
	good_block_list.add(good_block)
	all_sprites_list.add(good_block)
	bad_block_list.add(bad_block)
	all_sprites_list.add(bad_block)
# Create a RED player block
player = Player(BLUE, 5, 5, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			done = True
		
		# Set the speed based on the key pressed
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_RIGHT:
				player.changespeed(3, 0)
			elif event.key == pygame.K_UP:
				player.changespeed(0, -3)
			elif event.key == pygame.K_DOWN:
				player.changespeed(0, 3)
 
		# Reset speed when key goes up
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.changespeed(3, 0)
			elif event.key == pygame.K_RIGHT:
				player.changespeed(-3, 0)
			elif event.key == pygame.K_UP:
				player.changespeed(0, 3)
			elif event.key == pygame.K_DOWN:
				player.changespeed(0, -3)
 
	# Clear the screen
	screen.fill(WHITE)
 
	all_sprites_list.update()

	# See if the player block has collided with anything.
	blocks_hit_list = pygame.sprite.spritecollide(player, good_block_list, True)
 
	# Check the list of collisions.
	for block in blocks_hit_list:
		score += 1
		good_sound.play()
		print(score)
	
	blocks_hit_list = pygame.sprite.spritecollide(player, bad_block_list, True)
 
	# Check the list of collisions.
	for block in blocks_hit_list:
		score -= 1
		bad_sound.play()
		print(score)
 
	# Draw all the spites
	all_sprites_list.draw(screen)
	
	text = font.render('score: '+ str(score), True, BLACK)
	screen.blit(text, TEXT_POSITION)
 
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# Limit to 60 frames per second
	clock.tick(60)
 
pygame.quit()