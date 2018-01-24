import random

def min3(a,b,c):
	if a <= b and a <= c:
		return a 
	if b <= c and b <= a:
		return b 
	if c <= b and c <= a:
		return c 		
	
def box(height, cross):
	for i in range(height):
		for j in range(cross):
			print("*",end='')
		print()
	return 

def find(my_list,value):
	for i in range(len(my_list)):
		if my_list[i] == value:
			print("Found", value, "at position", i)
	return 
	
def create_list(size):
	my_list = []
	for i in range(size):
		my_list.append(random.randint(1,6))
	return my_list
	
def count_list(my_list, value):
	count = 0
	for i in my_list:
		if i == value:
			count += 1
	return count
	
def average_list(my_list):
	sum = 0
	for i in my_list:
		sum += i
	return float(sum/len(my_list))
	
def main():
	print(min3(4, 7, 5))
	print(min3(4, 5, 5))
	print(min3(4, 4, 4))
	print(min3(-2, -6, -100))
	print(min3("Z", "B", "A"))
	box(7,5)  # Print a box 7 high, 5 across
	print()   # Blank line
	box(3,2)  # Print a box 3 high, 2 across
	print()   # Blank line
	box(3,10) # Print a box 3 high, 10 across
	my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
	find(my_list, 12)
	find(my_list, 91)
	find(my_list, 80)
	my_list = create_list(5)
	print(my_list)
	count = count_list([1,2,3,3,3,4,2,1],3)
	print(count)
	avg = average_list([1,2,3])
	print(avg)
	my_list = create_list(1000)
	print( count_list(my_list,1) )
	print( count_list(my_list,2) )
	print( count_list(my_list,3) )
	print( count_list(my_list,4) )
	print( count_list(my_list,5) )
	print( count_list(my_list,6) )
	print( average_list(my_list) )

if __name__ == "__main__":
    main()