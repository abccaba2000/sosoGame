'''	Sketch

	Orientation :

		  N
		W	E
		  S

	Rooms Sketch :

	0					1
	-----------------	-----------------
	|				|	|				|
	|		This	|	|		Lab		|
	|				|	|				|
	-----------------	-----------------

	2					3
	-----------------	-----------------
	|				|	|				|
	|		Is		|	|		So		|
	|				|	|				|
	-----------------	-----------------

	4
	-----------------
	|				|
	|	Boring		|
	|				|
	-----------------

'''

room_list = []


'''	Create the Room List

	Implementation of each room :

		room = [Description, #North, #South, #West, #East]

'''

room = ["You're in 'This'. There is a passage to the south and the east.", None, 2, None, 1]
room_list.append(room)

room = ["You're in 'Lab'. There is a passage to the south and the west.", None, 3, 0, None]
room_list.append(room)

room = ["You're in 'Is'. There is a passage to the north, the south, and the east.", 0, 4, None, 3]
room_list.append(room)

room = ["You're in 'So'. There is a passage to the north and the west.", 1, None, 2, None]
room_list.append(room)

room = ["You're in 'Boring'. There is a passage to the north.", 2, None, None, None]
room_list.append(room)


# Yes, you are in Lab now.
cur_room = 1

done = False

while(not done) :

	print("\n\n")
	print(room_list[cur_room][0])
	
	print("n : Go North")
	print("s : Go South")
	print("w : Go West")
	print("e : Go East")
	dir = str(input("So, what do you want to do ?  "))
	
	if dir.upper() == 'N' :
		
		if(room_list[cur_room][1] != None) :
			cur_room = room_list[cur_room][1]
		else :
			print("\n\nHey, there is a wall.")

	elif dir.upper() == 'S' :
	
		if(room_list[cur_room][2] != None) :
			cur_room = room_list[cur_room][2]
		else :
			print("\n\nHey, there is a wall.")

	elif dir.upper() == 'W' :
	
		if(room_list[cur_room][3] != None) :
			cur_room = room_list[cur_room][3]
		else :
			print("\n\nHey, there is a wall.")

	elif dir.upper() == 'E' :
	
		if(room_list[cur_room][4] != None) :
			cur_room = room_list[cur_room][4]
		else :
			print("\n\nHey, there is a wall.")

	else :

		print("\n\nInvalid Direction.")
