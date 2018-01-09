# Import a library of functions called 'pygame'
import pygame
import random
import math
 
# Initialize the game engine
pygame.init()
 
# screen color
BLACK = [0, 0, 0]
# initial ball color
RED = [255, 0, 0]
# color chage when balls merge
COLOR_CHANGE = [-25, 25, 0]
# number of initial balls
NUMBER_OF_INITIAL_BALLS = 50

 
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
collide_count = []
collided_list = []
for i in range(NUMBER_OF_INITIAL_BALLS):
	collided_list.append([])
	for j in range(NUMBER_OF_INITIAL_BALLS):
		collided_list[i].append(0)
 
 


# Loop and add a ball in a random x,y position
ball_radius = BALL_RADIUS
for i in range(NUMBER_OF_INITIAL_BALLS):
	while True:
		x = random.randrange(ball_radius, WIDTH - ball_radius)
		y = random.randrange(ball_radius, HEIGHT - ball_radius)
		#if the ball covers another ball, find a new position 
		cover = False
		for j in range(len(ball_list)):
			if (x-ball_list[j][0])*(x-ball_list[j][0])\
			+ (y-ball_list[j][1])*(y-ball_list[j][1]) < 4*ball_radius*ball_radius:
				print('cover')
				cover = True
				break
		if cover:
			continue
		ball_list.append([x, y])
		ball_size.append(ball_radius)
		collide_count.append(1)
		dir_x = float(random.randrange(0, 3) - 1)
		dir_y = float(random.randrange(0, 3) - 1)
		directions.append([dir_x, dir_y])
		break

print(ball_list)
clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
	for event in pygame.event.get():   # User did something
		if event.type == pygame.QUIT:  # If user clicked close
			done = True   # Flag that we are done so we exit this loop
 
	# Set the screen background
	screen.fill(BLACK)
 
	#number of the ball
	ball_num = len(ball_list)
	# Process each ball in the list
	for i in range(ball_num):
 
		# Draw the ball
		pygame.draw.circle(screen, RED, ball_list[i], ball_size[i])
		# Draw the text
		font = pygame.font.SysFont('Calibri', ball_size[i], True, False)
		text = font.render(str(collide_count[i]), True, BLACK)
		screen.blit(text, [ball_list[i][0]-ball_size[i]+3, ball_list[i][1] - ball_size[i]+5])
 
		# If the ball  bump to edge of the screen, reflect
		if ball_list[i][0] >= WIDTH-ball_size[i]\
		   and directions[i][0] > 0:
			directions[i][0] *= -1
		elif ball_list[i][0] <= ball_size[i]\
			and directions[i][0] < 0:
			directions[i][0] *= -1
		if ball_list[i][1] >= HEIGHT-ball_size[i]\
		   and directions[i][1] > 0:
			directions[i][1] *= -1
		elif ball_list[i][1] <= ball_size[i]\
			and directions[i][1] < 0:
			directions[i][1] *= -1
			
	# If the balls each other collide, reflect
	for i in range(ball_num-1):
		for j in range(i+1,ball_num):
			x1 = ball_list[i][0]
			y1 = ball_list[i][1]
			x2 = ball_list[j][0]
			y2 = ball_list[j][1]
			if (x1-x2)*(x1-x2)	+ (y1-y2)*(y1-y2)\
			<= (ball_size[i]+ball_size[j])*(ball_size[i]+ball_size[j]):
				x_bump = x1-x2
				y_bump = y1-y2
				x_go1 = directions[i][0]
				y_go1 = directions[i][1]
				x_go2 = directions[j][0]
				y_go2 = directions[j][1]
				bump_unit1 = (x_go1*x_bump+y_go1*y_bump)/(x_bump*x_bump+y_bump*y_bump)
				bump_unit2 = (x_go2*x_bump+y_go2*y_bump)/(x_bump*x_bump+y_bump*y_bump)
				if x_bump > 0:
					directions[i][0] += 1
					directions[j][0] -= 1
				elif x_bump < 0:
					directions[i][0] -= 1
					directions[j][0] += 1
				if y_bump > 0:
					directions[i][1] += 1
					directions[j][1] -= 1
				elif y_bump < 0:
					directions[i][1] -= 1
					directions[j][1] += 1					
				#if bump_unit1 > 0:
				#	continue
				if collided_list[i][j] == 0:
					collided_list[i][j] += 1
					collide_count[i] += 1
					collide_count[j] += 1
				'''
				#print(bump_unit1,bump_unit2,x_bump,y_bump)
				#print('##', directions[i][0],directions[i][1],directions[j][0],directions[j][1])
				#print('&&',bump_unit2*x_bump,bump_unit2*y_bump,bump_unit1*x_bump,bump_unit1*y_bump)
				collided = False
				change_x1 = (bump_unit2*x_bump-bump_unit1*x_bump)
				if change_x1 > 0:
					change_x1 = math.ceil(change_x1)
				elif change_x1 < 0:
					change_x1 = math.floor(change_x1)
				change_y1 = (bump_unit2*y_bump-bump_unit1*y_bump)
				if change_y1 > 0:
					change_y1 = math.ceil(change_x1)
				elif change_y1 < 0:
					change_y1 = math.floor(change_x1)
				change_x2 = (bump_unit1*x_bump-bump_unit2*x_bump)
				if change_x2 > 0:
					change_x2 = math.ceil(change_x1)
				elif change_x2 < 0:
					change_x2 = math.floor(change_x1)				
				change_y2 = (bump_unit1*y_bump-bump_unit2*y_bump)
				if change_x2 > 0:
					change_x2 = math.ceil(change_x1)
				elif change_x2 < 0:
					change_x2 = math.floor(change_x1)				
				directions[i][0] += change_x1
				directions[i][1] += change_y1
				directions[j][0] += change_x2
				directions[j][1] += change_y2
				'''
			if collided_list[i][j] > 0:
				collided_list[i][j] += 1
			if collided_list[i][j] >= 5:
				collided_list[i][j] = 0
				#print('$$', directions[i][0],directions[i][1],directions[j][0],directions[j][1])
	# Move the ball	
	for i in range(ball_num):
		if directions[i][0] > 2:
			directions[i][0] = 1
		elif directions[i][0] < -2:
			directions[i][0] = -1
		if directions[i][1] > 2:
			directions[i][1] = 1
		elif directions[i][1] < -2:
			directions[i][1] = -1
		ball_list[i][0] += int(directions[i][0])
		ball_list[i][1] += int(directions[i][1])
	# Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	clock.tick(20)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()