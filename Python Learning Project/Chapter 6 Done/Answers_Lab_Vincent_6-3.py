n = int(input("Enter an integer : "))

for i in range(n) :
	for j in range(1 + 2*i, 2*n, 2) :
		print(j, end = " ")
	for space in range(2 * i) :
		print(end = "  ")
	for k in range(2*n - 1, 2*i, -2) :
		print(k, end = " ")
	print()

for i in range(n-1, -1, -1) :
	for j in range(1 + 2*i, 2*n, 2) :
		print(j, end = " ")
	for space in range(2 * i) :
		print(end = "  ")
	for k in range(2*n - 1, 2*i, -2) :
		print(k, end = " ")
	print()