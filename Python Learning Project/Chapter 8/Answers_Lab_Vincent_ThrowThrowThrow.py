import pygame
import math
import random

pygame.init()

done = False

DEBUG = 0

'''	Settings and Defaults '''

# Time Tracking
clock = pygame.time.Clock()


# Screen Settings
ScreenSize = (800, 600)
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Throw Throw Throw")


# Color Definition
Color_White = (255, 255, 255)
Color_Black = (0, 0, 0)


# Object Settings

## Others
Pos_SpinCenter = [int(ScreenSize[0] / 2), int(ScreenSize[1] / 4)]
Factor_Gravity = 1.5

## Stick
Len_Stick = int(ScreenSize[0] * ScreenSize[1] / 5000)
Width_Stick = int(Len_Stick / 30)
Pos_Stick_start = Pos_SpinCenter
Pos_Stick_end = [Pos_Stick_start[0] + Len_Stick, Pos_Stick_start[1]]
Ang_Stick = 0.1
Ang_Stick_change = 0.05

## Flake
Radi_Flake = int(Len_Stick / 10)
Width_Flake = Width_Stick

### List_Flakes = [Pos_x, Pos_y, Vel_x, Vel_y, Moving_Condition]
#### Moving_Condition :		0	Spining
####						1	Moving
####						2	Static
List_Flakes = []

Vel_Flake_Raw_Min = 10
Vel_Flake_Raw_Max = 5000
Scale_Flake_Vel = 100

## Wall
Factor_Bounce_X = -0.8
Factor_Bounce_Y = -0.5


# Conditions

Is_Flake_ToGenerate = 1
Accuracy_Flake_LaunchPos = 100
Is_Flake_AllowLaunch = 0
Is_Flake_Launched = 1
Ang_Flake_Launch = 0

## Moving Conditions

Cdt_Spining = 0
Cdt_Moving = 1
Cdt_Static = 2


''' Main Game Loop '''

while not done :


	'''	Event Response '''

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			done = True
			continue


	'''	Drawing '''
	
	screen.fill(Color_White)
	

	for index in range(len(Pos_Stick_end)) :
		Pos_Stick_end[index] = int(Pos_Stick_end[index])

	pygame.draw.line(screen, Color_Black, Pos_Stick_start, Pos_Stick_end, Width_Stick)


	
	print(List_Flakes)

	for flakes in List_Flakes :

		flakes_temp_for_int = []
		for index_flakes in flakes[:2] :
			flakes_temp_for_int.append(int(index_flakes))

		pygame.draw.circle(screen, Color_Black, flakes_temp_for_int, Radi_Flake, Width_Flake)
	

	
	# Fliping
	pygame.display.flip()

	


	''' Animation Calculation '''

	# Spin of Stick
	
	Pos_Stick_end[0] = Pos_SpinCenter[0] + Len_Stick * math.sin(Ang_Stick)
	Pos_Stick_end[1] = Pos_SpinCenter[1] + Len_Stick * math.cos(Ang_Stick)

	Ang_Stick += Ang_Stick_change

	if Ang_Stick > 2 * math.pi :
		Ang_Stick -= 2 * math.pi

	
	# Flake Control

	## Generate New Flake

	if Is_Flake_ToGenerate and Is_Flake_Launched :
		
		Is_Flake_Launched = 0;

		Vel_Flake_Scaled_X = random.randrange(Vel_Flake_Raw_Min, Vel_Flake_Raw_Max, 1) / Scale_Flake_Vel
		Vel_Flake_Scaled_Y = random.randrange(Vel_Flake_Raw_Min, Vel_Flake_Raw_Max, 1) / Scale_Flake_Vel

		if random.randrange(2) :

			Vel_Flake_Scaled_X *= -1

		if random.randrange(2) :

			Vel_Flake_Scaled_Y *= -1


		New_Flake = [Pos_Stick_end[0], Pos_Stick_end[1], Vel_Flake_Scaled_X, Vel_Flake_Scaled_Y, Cdt_Spining]

		List_Flakes.append(New_Flake)
	
		if DEBUG :

			print("Length of List = ", len(List_Flakes), end = "\t")
			print(List_Flakes)

		### The moment flake leave the stick, defined by angle.
		Ang_Flake_Launch = random.randrange(Accuracy_Flake_LaunchPos) / Accuracy_Flake_LaunchPos * (2 * math.pi) 

		Is_Flake_ToGenerate = False

		Is_Flake_AllowLaunch = True


	## Moving Permission

	if abs(Ang_Stick - Ang_Flake_Launch) <= Ang_Stick_change and Is_Flake_AllowLaunch:
		
		#### Allow the Flake Moving
		List_Flakes[len(List_Flakes) - 1][4] = Cdt_Moving
		
		Is_Flake_Launched = 1

		
	
	## Moving

	for index in range(len(List_Flakes)) :


		### If in Moving Condition, then Moving

		if List_Flakes[index][4] == Cdt_Moving :

			List_Flakes[index][0] += List_Flakes[index][2]
			List_Flakes[index][1] += List_Flakes[index][3]

			### Gravity Simulation
			List_Flakes[index][3] += Factor_Gravity
		

		elif List_Flakes[index][4] == Cdt_Spining :

			List_Flakes[index][0] = Pos_Stick_end[0]
			List_Flakes[index][1] = Pos_Stick_end[1]

		
		




	## Bouncing

	for flakes in List_Flakes :

		### Horizontal Bounce

		if flakes[0] + Radi_Flake >= ScreenSize[0] :

			flakes[0] = ScreenSize[0] - Radi_Flake
			flakes[2] *= Factor_Bounce_X


		elif flakes[0] - Radi_Flake <= 0 :

			flakes[0] = Radi_Flake
			flakes[2] *= Factor_Bounce_X


		### Vertical Bounce

		if flakes[1] + Radi_Flake >= ScreenSize[1] :

			flakes[1] = ScreenSize[1] - Radi_Flake
			flakes[3] *= Factor_Bounce_Y
			flakes[2] *= abs(Factor_Bounce_X)

		elif flakes[1] - Radi_Flake <= 0 :

			flakes[1] = Radi_Flake
			flakes[3] *= Factor_Bounce_Y
			flakes[2] *= abs(Factor_Bounce_X)


		#### If touch the ground and the next flake is launched, prepare the next flake

		
		if ScreenSize[1] - flakes[1] <  1.5 * Radi_Flake and abs(flakes[2] * flakes[3]) < 0.5 :

			Is_Flake_ToGenerate = True

			flakes[1] = ScreenSize[1] - Radi_Flake
			flakes[2] = 0
			flakes[3] = 0
			flakes[4] = Cdt_Static




	''' Frame Rate Control '''
	clock.tick(20)



''' Quit Game '''

pygame.quit()