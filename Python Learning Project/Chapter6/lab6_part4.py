# Import a library of functions called 'pygame'
import pygame
# For using 'pi' and sqrt
import math
# Initialize the game engine
pygame.init()
# Define some colors
GREEN = (0, 255, 0)
#Define height and width
HEIGHT = 750
WIDTH = 600 
# Set the height width, title of the screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
# Loop as long as done == False
while not done:
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
	for i in range(0,HEIGHT):
		for j in range(0, WIDTH):
			if i%8 == 0 and j%8 == 0:
				pygame.draw.rect(screen, GREEN, [j,i,4,4], 0)
	
	# display all the thing we drawn
	pygame.display.flip()
 	# This limits the while loop to a max of 60 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(60)
# Be IDLE friendly
pygame.quit()