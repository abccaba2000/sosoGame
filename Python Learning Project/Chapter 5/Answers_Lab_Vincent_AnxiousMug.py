import pygame
pygame.init()
import random
import math

# Color Definition
COLOR_ANXIOUS_MUG = (160, 32, 240)
COLOR_ROAD = (250, 250, 210)
COLOR_GRASS = (124, 252, 0)
COLOR_SKY = (135, 206, 250)
COLOR_SUN = (255, 69, 0)
COLOR_RAIN = (25, 25, 112)

# Set Screen
screen_size = (1200, 800)
screen = pygame.display.set_mode(screen_size)

# Area of Grass
area_grass_pos_x = 0
area_grass_pos_y = int(screen_size[1] / 3)
area_grass_size_width = screen_size[0]
area_grass_size_height = int(screen_size[1] / 3 * 2)

grass_area = [
	area_grass_pos_x,
	area_grass_pos_y,
	area_grass_size_width,
	area_grass_size_height
]

# Area of Road
area_road_size_width = screen_size[0]
area_road_size_height = int(area_grass_size_height / 4)
area_road_pos_x = 0
area_road_pos_y = int(area_grass_pos_y + (area_grass_size_height - area_road_size_height) / 2)

road_area = [
	area_road_pos_x,
	area_road_pos_y,
	area_road_size_width,
	area_road_size_height
]

# Area of the Sun
area_sun_pos_x = int(screen_size[0] / 6 * 5)
area_sun_pos_y = int(screen_size[1] / 9)
area_pos = [area_sun_pos_x, area_sun_pos_y]
area_sun_radius = int((screen_size[0] * screen_size[1]) / 20000)

# Rain Drop
drop_size_width = int(screen_size[0] / 1000)
drop_size_height = int(screen_size[1] / 100)

# Area of Anxious Mug
area_mug_handle_size_width = int(screen_size[0] / 25 )
area_mug_handle_size_height = int(screen_size[1] / 16 )
area_mug_handle_pos_y = int(area_road_pos_y + (area_road_size_height - area_mug_handle_size_height) / 2)
angle_mug_handle_start = math.pi / 2
angle_mug_handle_end = math.pi * 3 / 2
width_mug_handle = int(area_mug_handle_size_width * area_mug_handle_size_height / 400)
area_mug_body_size_width = int(area_mug_handle_size_width * 2)
area_mug_body_size_height = int(area_mug_handle_size_height)
area_mug_bottom_size_width = int(area_mug_body_size_width)
area_mug_bottom_size_height = int(area_mug_body_size_height * 2)
<<<<<<< HEAD:Python Learning Project/Chapter 5/Answers_Lab_Vincent_AnxiousMug.py
#area_mug_handle_pos_y = int(area_road_pos_y + (area_road_size_height - area_mug_bottom_size_height) / 2)
=======
#area_mug_handle_pos_y = int(area_road_pos_y + (area_road_size_height - area_mug_bottom_size_width) / 2)
>>>>>>> ef96c806e00d246551966d789d3979b904bde4cb:Python Learning Project/Chapter5/lab.py

# Game Loop
done = False
clock = pygame.time.Clock()
area_mug_handle_pos_x = 0
mug_next = random.randrange(0, screen_size[0] - area_mug_body_size_width)

while not done :

	# Event Response
	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			done = True
			continue
	
	#draw Background
	screen.fill(COLOR_SKY)
	pygame.draw.rect(screen, COLOR_GRASS, grass_area, 0)
	pygame.draw.rect(screen, COLOR_ROAD, road_area, 0)
	pygame.draw.circle(screen, COLOR_SUN, area_pos, area_sun_radius, 0)

	# Draw Rain
	for rain_count in range(50) : 

		# Randomly create the position of each rain. 
		drop_rect = [
			random.randrange(screen_size[0]),
			random.randrange(screen_size[1]),
			drop_size_width,
			drop_size_height
		]
		pygame.draw.rect(screen, COLOR_RAIN, drop_rect, 0)

	# Draw Anxious Mug

	## Set stance of Mug (Screen Size Dependent).
	mug_max_stance = int(screen_size[0]/100)
	
	## Decide the direction to go.
	if(area_mug_handle_pos_x < mug_next) :
		area_mug_handle_pos_x += random.randrange(mug_max_stance)
	else :
		area_mug_handle_pos_x += -random.randrange(mug_max_stance)

	## Set new goal.
	if abs(area_mug_handle_pos_x - mug_next) < mug_max_stance / 10: 
		mug_next = random.randrange(0, screen_size[0] - area_mug_body_size_width, 100)

	## Draw Anxious Mug - Handle
	pygame.draw.arc(screen, COLOR_ANXIOUS_MUG, 
		(area_mug_handle_pos_x, area_mug_handle_pos_y, area_mug_handle_size_width, area_mug_handle_size_height),
		angle_mug_handle_start, angle_mug_handle_end, width_mug_handle)

	## Draw Anxious Mug - Body
	pos_mug_body_x = int(area_mug_handle_pos_x + area_mug_handle_size_width / 2)
	pos_mug_body_y = int(area_mug_handle_pos_y)
	pygame.draw.rect(screen, COLOR_ANXIOUS_MUG, 
		(pos_mug_body_x, pos_mug_body_y, area_mug_body_size_width, area_mug_body_size_height), 0)

	## Draw Anxious Mug - Bottom
	pos_mug_bottom_x = pos_mug_body_x
	pos_mug_bottom_y = pos_mug_body_y
	pygame.draw.ellipse(screen, COLOR_ANXIOUS_MUG,
		(pos_mug_bottom_x, pos_mug_bottom_y, area_mug_bottom_size_width, area_mug_bottom_size_height), )

	# Fliping
	pygame.display.flip()

	# Frame Rate
	clock.tick(20)

# Quit the game properly
pygame.quit()
