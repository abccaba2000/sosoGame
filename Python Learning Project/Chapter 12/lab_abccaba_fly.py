import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

 
class Rectangle():
	def __init__(self):
		self.x = random.randint(0,700)
		self.y = random.randint(0,500)
		self.height = random.randint(20,70)
		self.width = random.randint(20,70)
		self.red = random.randint(0,255)
		self.green= random.randint(0,255)
		self.blue = random.randint(0,255)
		self.change_x = random.randint(-3,3)
		self.change_y = random.randint(-3,3)
		
	def draw(self, screen):
		pygame.draw.rect(screen, (self.red, self.green, self.blue), [self.x, self.y, self.width, self.height])
	
	def move(self):
		self.x += self.change_x
		self.y += self.change_y

class Ellipse(Rectangle):
	def __init__(self):
		super().__init__()
		
	def draw(self, screen):
		pygame.draw.ellipse(screen, (self.red, self.green, self.blue), [self.x, self.y, self.width, self.height])

		
rects = []
ellipses = []
fly_n = 20
for i in range(fly_n):
	rect_obj = Rectangle()
	ellipse_obj = Ellipse()
	rects.append(rect_obj)
	ellipses.append(ellipse_obj)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Fly")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	# --- Screen-clearing code goes here
 
	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
 
	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(BLACK)
			
	# --- Game logic should go here
	for i in range(fly_n):
		rects[i].draw(screen)
		ellipses[i].draw(screen)
		rects[i].move()
		ellipses[i].move()
	
	

 
	# --- Drawing code should go here
 
	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
 
	# --- Limit to 60 frames per second
	clock.tick(60)
 
# Close the window and quit.
pygame.quit()