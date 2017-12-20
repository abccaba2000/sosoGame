n = int(input("Enter a integer : "))

for top in range(2*n) :
	print("o", end = "")
print()

for j in range(n-2) : 
	for i in range(2*n) :
		if(i == 0 or i == 2*n - 1) :
			print("o", end = "")
		else :
			print(end = " ")
	print()

for bottom in range(2*n) :
	print("o", end = "")