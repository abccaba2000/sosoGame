import random

print('Welcome to Camel!')
print('You have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down!')
print('Survive your desert trek and out run the natives.')

done = False

travel = thirst = tired = 0
native = -20
drinks = 3

while done == False:
	print('\n')
	print('A. Drink from your canteen.')
	print('B. Ahead moderate speed.')
	print('C. Ahead full speed.')
	print('D. Stop for the night.')
	print('E. Status check.')
	print('F. Soso')
	print('Q. Quit.')
	
	choice = input('')
	choice = choice.upper()
	
	print('\n')
	
	if choice == 'Q':
		done = True
	elif choice == 'E':
		print('Miles traveled:',travel)
		print('Drinks in canteen:',drinks)
		print('The natives are '+str(travel-native)+' miles behind you.')	
	elif choice == 'D':
		tired = 0
		print('the camel is happy')
		native += random.randrange(7,15)
	elif choice == 'C':
		travel += random.randrange(10,21)
		print('You have traveled for '+ str(travel) +' miles')
		thirst += 1
		tired += random.randrange(1,3)
		native += random.randrange(7,15)
	elif choice == 'B':
		travel += random.randrange(5,13)
		print('You have traveled for '+ str(travel) +' miles')
		thirst += 1
		tired += 1
		native += random.randrange(7,15)		
	elif choice == 'A':
		if drinks > 0:
			drinks -= 1
			thirst = 0
		else:
			print('GG, no drink in the canteen.')
	elif choice == 'F':
		input('What\'s your dream?')
		thirst += 2
		native += random.randrange(7,15)
		print('OK, The natives are closer.')
	if thirst > 4:
		if thirst > 6:
			print('You died of thirst!')
			done = True
		else:	print('You are thirsty.')
	if tired > 5:
		if tired > 8:
			print('Your camel is dead.')
			done = True
		else:	print('Your camel is getting tired.')
	if native+15 >= travel:
		if native >= travel:
			print('The natives caught the player')
			done = True
		else:
			print('The natives are getting close!')
	if travel >= 200 and not done:
		print('You win!! You made it even you are a sosoker!')
		done = True
	
	
	if not random.randrange(20) and (choice == 'B' or choice == 'C'):
		print('You found an oasis!')
		thirst = tired = 0
		drinks = 3

input('sosoker is quiting...')
