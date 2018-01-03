# Import a library of functions called 'pygame'
import pygame
import random
 
# Initialize the game engine
pygame.init()
 
# screen color
BLACK = [0, 0, 0]
# initial ball color
RED = [255, 0, 0]
# color chage when balls merge
COLOR_CHANGE = [-25, 25, 0]
# number of initial balls
NUMBER_OF_INITIAL_BALLS = 32

 
# Set the height and width of the screen
HEIGHT = 600
WIDTH = 800
size = [WIDTH, HEIGHT]

#Set the initial size of balls
BALL_RADIUS = 16


 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bump into your heart")
 
# Create an empty array
ball_list = []
ball_size = []
directions = []
 
 


# Loop and add a ball in a random x,y position
ball_radius = BALL_RADIUS
for i in range(NUMBER_OF_INITIAL_BALLS):
	x = random.randrange(ball_radius, HEIGHT - ball_radius)
	y = random.randrange(ball_radius, WIDTH - ball_radius)
	ball_list.append([x, y])
	ball_size.append(ball_radius)
	dir_x = random.randrange(0, 3) - 1
	dir_y = random.randrange(0, 3) - 1
	directions.append([dir_x, dir_y])

 
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
	for event in pygame.event.get():   # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True   # Flag that we are done so we exit this loop
 
	# Set the screen background
	screen.fill(BLACK)
 
	# Process each ball in the list
	for i in range(len(ball_list)):
 
		# Draw the ball
		pygame.draw.circle(screen, RED, ball_list[i], ball_size[i])
		# Draw the text
		font = pygame.font.SysFont('Calibri', ball_size[i]*2, True, False)
		text = font.render(str(int(ball_size[i]/BALL_RADIUS)), True, BLACK)
		screen.blit(text, [ball_list[i][0]-ball_size[i]/2, ball_list[i][1] - ball_size[i]])
		
		# Move the ball down one pixel
		ball_list[i][0] += directions[i][0]
		ball_list[i][1] += directions[i][1]
 
		# If the ball has moved off the bottom of the screen
		if ball_list[i][0] > WIDTH-ball_size[i] \
		   or ball_list[i][0] < ball_size[i]:
			directions[i][0] *= -1
		if ball_list[i][1] > HEIGHT-ball_size[i] \
		   or ball_list[i][1] < ball_size[i]:
			directions[i][1] *= -1
			

	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()