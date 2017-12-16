print("\n\nWelcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives.")

done = False
import random

miles_player = 0
thirst = 0
tiredness = 0 # of camel
miles_native = -20
drinks = 10 #in canteen

while(not done) :

	print("\n\n\nA. Drink from your canteen.")
	print("B. Ahead moderate speed.")
	print("C. Ahead full speed!!")
	print("D. Stop for the night.")
	print("E. Status check.")
	print("Q. Quit.\n")

	cmd = input("Your choice is : ")

	if(cmd.upper() == 'Q') :
		done = True
	elif(cmd.upper() == 'E') :
		print("Miles travels : ", miles_player)
		print("Drinks in canteen : ", drinks)
		print("The natives are ", miles_player - miles_native, "behind you.")
	elif(cmd.upper() == 'D') : 
		tiredness = 0
		print("Camel is happy but worried...")
		miles_native += random.randrange(7, 15)
	elif(cmd.upper() == 'C') :
		miles_player += random.randrange(10,21)
		print("You've traveled ", miles_player)
		thirst += 1
		tiredness += random.randrange(1, 4)
		miles_native += random.randrange(7, 15)
	elif(cmd.upper() == 'B') :
		miles_player += random.randrange(5, 13)
		print("You've traveled ", miles_player)
		thirst += 1
		tiredness += 1
		miles_native += random.randrange(7, 15)
	elif(cmd.upper() == 'A') :
		if(drinks > 0) :
			drinks -= 1
			thirst = 0
		else :
			print("Canteen is empty...qq")
	
	if(random.randrange(20) == 0) :
		print("Find oasis!!! You are energetic now !")
		drinks = 10
		thirst = 0
		tiredness = 0

	if(thirst > 6 and not done) :
		print("You've dead... Diagnosis : thirst")
		done = True
	elif(thirst > 4) :
		print("Feel thirsty...")

	if(tiredness > 8 and not done) :
		print("Your (stolen) camel is dead.")
		done = True
	elif(tiredness > 5) :
		print("Your (stolen) camel is getting tired.")
	
	if(miles_native >= miles_player and not done) : 
		print("You've been caught...")
		print("Game Over, Goodbye")
		done = True
	elif(miles_player - miles_native < 15) : 
		print("The natives are near here")

	if(miles_player >= 200 and not done) :
		print("You've out run from the desert!!")
		print("The camel is yours!")
	