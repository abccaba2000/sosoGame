# Import a library of functions called 'pygame'
import pygame
# For using 'pi' and sqrt
import math

# Initialize the game engine
pygame.init()

# Define some colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#define 'pi' and sqrt of 3
PI = math.pi
SQRT_3 = math.sqrt(3)
#Define height and width
HEIGHT = 750
WIDTH = 600 


# Set the height width, title of the screen
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Let me draw you a dream")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
	for event in pygame.event.get():  # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True  # Flag that we are done so we exit this loop
 
	# All drawing code happens after the for loop and but
	# inside the main while not done loop.
 
	# Clear the screen and set the screen background
	screen.fill(WHITE)
	center_h = HEIGHT/2
	center_w = WIDTH/2
	edge = 300
	reverse = 1
	tri_a = [center_w, center_h - reverse*(edge/SQRT_3)]
	tri_b = [center_w - edge/2, center_h + reverse*(edge/SQRT_3/2)]
	tri_c = [center_w + edge/2, center_h + reverse*(edge/SQRT_3/2)]
	color = BLACK
	pygame.draw.polygon(screen, color, [tri_a, tri_b, tri_c], 5)
	for i in range(4):
		edge_1 = edge/2
		reverse_1 = reverse
		center_h_1 = center_h
		center_w_1 = center_w
		if i == 0:
			reverse_1 *= -1
			color = RED
		elif i == 1:
			center_h_1 = (center_h + tri_a[1])/2
		elif i == 2:
			center_h_1 = (center_h + tri_b[1])/2
			center_w_1 = (center_w + tri_b[0])/2
		elif i == 3:
			center_h_1 = (center_h + tri_c[1])/2
			center_w_1 = (center_w + tri_c[0])/2
		tri_a_1 = [center_w_1, center_h_1 - reverse_1*(edge_1/SQRT_3)]
		tri_b_1 = [center_w_1 - edge_1/2, center_h_1 + reverse_1*(edge_1/SQRT_3/2)]
		tri_c_1 = [center_w_1 + edge_1/2, center_h_1 + reverse_1*(edge_1/SQRT_3/2)]
		if i == 0:
			pygame.draw.polygon(screen, color, [tri_a_1, tri_b_1, tri_c_1], 5)
		for j in range(4):
				edge_2 = edge_1/2
				reverse_2 = reverse_1
				center_h_2 = center_h_1
				center_w_2 = center_w_1
				if j == 0:
					reverse_2 *= -1
					color = GREEN
				elif j == 1:
					center_h_2 = (center_h_1 + tri_a_1[1])/2
				elif j == 2:
					center_h_2 = (center_h_1 + tri_b_1[1])/2
					center_w_2 = (center_w_1 + tri_b_1[0])/2
				elif j == 3:
					center_h_2 = (center_h_1 + tri_c_1[1])/2
					center_w_2 = (center_w_1 + tri_c_1[0])/2
				tri_a_2 = [center_w_2, center_h_2 - reverse_2*(edge_2/SQRT_3)]
				tri_b_2 = [center_w_2 - edge_2/2, center_h_2 + reverse_2*(edge_2/SQRT_3/2)]
				tri_c_2 = [center_w_2 + edge_2/2, center_h_2 + reverse_2*(edge_2/SQRT_3/2)]
				if j == 0:
					pygame.draw.polygon(screen, color, [tri_a_2, tri_b_2, tri_c_2], 5)
				for k in range(4):
						edge_3 = edge_2/2
						reverse_3 = reverse_2
						center_h_3 = center_h_2
						center_w_3 = center_w_2
						if k == 0:
							reverse_3 *= -1
							color = BLUE
						elif k == 1:
							center_h_3 = (center_h_2 + tri_a_2[1])/2
						elif k == 2:
							center_h_3 = (center_h_2 + tri_b_2[1])/2
							center_w_3 = (center_w_2 + tri_b_2[0])/2
						elif k == 3:
							center_h_3 = (center_h_2 + tri_c_2[1])/2
							center_w_3 = (center_w_2 + tri_c_2[0])/2
						tri_a_3 = [center_w_3, center_h_3 - reverse_3*(edge_3/SQRT_3)]
						tri_b_3 = [center_w_3 - edge_3/2, center_h_3 + reverse_3*(edge_3/SQRT_3/2)]
						tri_c_3 = [center_w_3 + edge_3/2, center_h_3 + reverse_3*(edge_3/SQRT_3/2)]
						if k == 0:
							pygame.draw.polygon(screen, color, [tri_a_3, tri_b_3, tri_c_3], 5)
	color = [255, 0, 0]
	edge = 500
	h = center_h-edge/2
	w = center_w-edge/2
	for i in range(0, 100):
		pygame.draw.arc(screen, color, [w, h, edge, edge], i/10, i/10+0.2, 3)
		if color[0] > 0:
			color[0] -= 5
			color[1] += 5
		else:
			color[1] -= 5
			color[2] += 5
		h += 1
		w += 1
		edge -= 2
		
	
	# Go ahead and update the screen with what we've drawn.
	# This MUST happen after all the other drawing commands.
	pygame.display.flip()
 
	# This limits the while loop to a max of 60 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(60)
 
# Be IDLE friendly
pygame.quit()