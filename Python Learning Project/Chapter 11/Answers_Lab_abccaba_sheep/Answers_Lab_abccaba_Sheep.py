
import pygame
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


BACKGROUND_Y_SHIFT = 168
SCREEN_SIZE = [432, 600]
SHEEP_SIZE = 52
GROUND_Y = SCREEN_SIZE[1] - 4*int(SHEEP_SIZE/5)
SHEEP_INITIAL_POSITION = [int(SCREEN_SIZE[0]/2), GROUND_Y]
TEXT_SIZE = 25
TEXT_POSITION = [int( SCREEN_SIZE[0]/2-TEXT_SIZE ), int( SCREEN_SIZE[1]/3 )]

 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode(SCREEN_SIZE)
 
# This sets the name of the window
pygame.display.set_caption('Sheep')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
sound = pygame.mixer.Sound("yisell_sound.ogg")
 
# Set positions of graphics
background_position = [0, -BACKGROUND_Y_SHIFT]
 
# Load and set up graphics.
background_image = pygame.image.load("grass.jpg").convert()
background_image2 = pygame.image.load("Chain'sDoubleJaw.jpg").convert()
sheep = pygame.image.load("sheep_red.png").convert()
sheep = pygame.transform.scale(sheep, (52, 52))
sheep.set_colorkey(RED)

font = pygame.font.SysFont('Calibri', TEXT_SIZE, True, False)
 
done = False
double_jaw = False
 
sheep_pos = SHEEP_INITIAL_POSITION
move = [0,0]

hit_count = 0  

 
while not done:
	
	jump = False
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			edge_size = int(SHEEP_SIZE/5)
			player_position = pygame.mouse.get_pos()
			x = player_position[0]
			y = player_position[1]
			if x >= sheep_pos[0]+edge_size and x <= sheep_pos[0]+SHEEP_SIZE-edge_size and y >= sheep_pos[1]+edge_size and y <= sheep_pos[1]+SHEEP_SIZE-edge_size:
				jump = True
				hit_count += 1
				if hit_count == 5:
					double_jaw = True
				sound.play()
 
	# Copy image to screen:
	if double_jaw:
		screen.blit(background_image2, background_position)
	else:
		screen.blit(background_image, background_position)
 
	# Get the current mouse position. This returns the position
	# as a list of two numbers.

	text = font.render(str(hit_count), True, BLACK)
	screen.blit(text, TEXT_POSITION)
	
	# Copy image to screen:
	if jump:
		move[1] = -20
		
	sheep_pos[0] += move[0]
	sheep_pos[1] += move[1]
	
	move[1] += 1
	if sheep_pos[1] >= GROUND_Y:
		sheep_pos[1] = GROUND_Y
		move[1] = 0
		hit_count = 0
		double_jaw = False
	
	screen.blit(sheep, sheep_pos)
 
	pygame.display.flip()
 
	clock.tick(20)
 
pygame.quit()