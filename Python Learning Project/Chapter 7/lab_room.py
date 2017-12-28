# soso something about this game
print('Hello Vicent, you are locked in a building, you should go around and figure out how to escape here.')

#define all the room in the list
room_list = [['empty room',1, None, None, None],\
			['restaurant',3,2,0,None],\
			['dark room',None,None,None,1],\
			['warehouse',None,None,1,None],\
			['secret room',None,None,None,0]]

#initialize the position, item
current_room = 0
item = []
done = False

while not done:
	
	#print the current state
	print('You are in the ' + room_list[current_room][0])
	print('Your item:', item)
	
	#if in the empty room
	if current_room == 0 :
		#if you have book, the secret door to the fifth room will open
		if 'book' in item:
			print('You read the soso on the book and hear a loud sound. The secret door to the north is open!')
			room_list[0][2] = 4
		#no book no soso
		else:
			print('there is nothing here. You should move!')
	#if in the restaurant
	elif current_room == 1:
		# get the candle if you don't have it
		if 'candle' not in item and 'lighted candle' not in item:
			print('You eat the chicken and take the candle on the table')
			item.append('candle')
			print('Your item:', item)
		# guide the player. There is two possible way to go 
		print('The room to the north seems very dark.The room to the west seems very stinky')
	# if in the dark room	
	elif current_room == 2:
		# no candle, too dark
		if 'lighted candle' not in item:
			print('This is so dark here, so dark to die')
			input('You lose. What\'s your comment? ')
			break
		# you have a candle, you find a book
		else:
			print('Thanks for the light of the candle, You fin d a book with a lot of soso in it!')
			item.append('book')
			print('Your item:', item)
	# if in the warehouse
	elif current_room == 3:
		#if no fired candle, fire it
		if 'candle' in item:	
			print('You use a lighter here light the candle')
			item.remove('candle')
			item.append('lighted candle')
			print('Your item:', item)
	# if in the secret room
	elif current_room == 4:
		
		print('There is a terrifying monster sitting in the room!! He opens his mouth with bloody teeth:')
		print('"I didn\'t expect you can succeed to be in front of me. Now, if you answer my question right, I let you go"')
		
		# get the answer and win the game
		while True:
			response = input("Who is the master of 3D printing?: ")
			if response == 'Dehan' or response == 'dehan':
				input('Coreect! You win!')
				done == True
				break
			else:
				choice = input('Wrong! Do you want to die or I give you another chance?(die/chance): ')
				if choice == 'die':
					input('You lose. What\'s your comment? ')
					done == True
					break
		if done: break
	#Let the player move
	while True:
		#tell the player the doors to another room
		if room_list[current_room][1] != None:
			print('There is a door to the east')
		if room_list[current_room][2] != None:
			print('There is a door to the north')
		if room_list[current_room][3] != None:
			print('There is a door to the west')			
		if room_list[current_room][4] != None:
			print('There is a door to the south')

		#Let the player choose where to go 
		direction = input('which direction do you want to go?: ')
		if direction == 'e' and room_list[current_room][1] != None:
			current_room = room_list[current_room][1]
			break
		elif direction == 'n' and room_list[current_room][2] != None:
			current_room = room_list[current_room][2]
			break
		elif direction == 'w' and room_list[current_room][3] != None:
			current_room = room_list[current_room][3]
			break
		elif direction == 's' and room_list[current_room][4] != None:
			current_room = room_list[current_room][4]
			break
		else:
			print('you can not go this way')
	
	# seperate each round
	print()