 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
 
def draw_stick_figure(screen, x, y, body_color):
	# Head
	pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
	# Legs
	pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
	pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
	# Body
	pygame.draw.line(screen, body_color, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
	# Arms
	pygame.draw.line(screen, body_color, [5 + x, 7 + y], [9 + x, 17 + y], 2)
	pygame.draw.line(screen, body_color, [5 + x, 7 + y], [1 + x, 17 + y], 2)
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("I am QQ")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10
# -------- Main Program Loop -----------
while not done:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			# User pressed down on a key
 
		elif event.type == pygame.KEYDOWN:
			# Figure out if it was an arrow key. If so
			# adjust speed.
			if event.key == pygame.K_LEFT:
				x_speed = -3
			elif event.key == pygame.K_RIGHT:
				x_speed = 3
			elif event.key == pygame.K_UP:
				y_speed = -3
			elif event.key == pygame.K_DOWN:
				y_speed = 3
 
		# User let up on a key
		elif event.type == pygame.KEYUP:
			# If it is an arrow key, reset vector back to zero
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_speed = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_speed = 0
 
	# --- Game Logic
 
	# Move the object according to the speed vector.
	x_coord = x_coord + x_speed
	y_coord = y_coord + y_speed
 
	# ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
	# ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
 
	# Call draw stick figure function
	pos = pygame.mouse.get_pos()
	x = pos[0]
	y = pos[1]
 
	
	if x <= 0:
		x = 0
	if y <= 0:
		y = 0
	if x >= 700-10:
		x = 700-10
	if y >= 500-27:
		y = 500-27
	if x_coord <= 0:
		x_coord = 0
	if y_coord <= 0:
		y_coord = 0
	if x_coord >= 700-10:
		x_coord = 700-10
	if y_coord >= 500-27:
		y_coord = 500-27	
	
	# ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
	# ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(WHITE)
	draw_stick_figure(screen, x, y, RED)
	draw_stick_figure(screen, x_coord, y_coord, GREEN)
	# ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# Limit to 20 frames per second
	clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()