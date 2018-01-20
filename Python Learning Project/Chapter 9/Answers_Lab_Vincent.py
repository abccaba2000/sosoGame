'''	Question 1
'''

def min3(a, b, c) :

	if a <= b and a <= c :
		return a

	elif b <= a and b <= c :
		return b

	else :
		return c

'''	Test Code

print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))

'''


'''	Question 2
'''

def box(row, col) :

	for i in range(row) :
		for j in range(col) :
			print('*', end = '')
		print()

'''	Test Code

box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

'''


'''	Question 3
'''

def find(my_list, key) :

	for index in range(len(my_list)) :
		if key == my_list[index] :
			print("Found", key, "at position", index)




'''	Test Code

my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
 
find(my_list, 12)
find(my_list, 91)
find(my_list, 80)

'''


'''	Question 4-1=1
'''

import random

def create_list(size) :

	new_list = []

	for index in range(size) :
		new_list.append(random.randrange(1, 7))

	return new_list


'''	Test Code

my_list = create_list(5)
print(my_list)

'''


'''	Question 4-1-2
'''

def count_list(list, key) :
	
	count = 0

	for item in list :
		if item == key :
			count += 1

	return count


'''	Test Code

count = count_list([1,2,3,3,3,4,2,1],4)
print(count)

'''


'''	Question 4-1-3
'''

def average_list(list) :

	sum = 0

	for item in list :
		sum += item

	return sum/len(list)


'''	Test Code

avg = average_list([1,2,3])
print(avg)

'''


'''	Question 4-2
'''

list = create_list(10000)

for index in range(1, 7) :
	print(count_list(list, index))

print(average_list(list))


