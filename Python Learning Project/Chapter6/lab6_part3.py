n = int(input('n= '))
if n >= 2:
	for i in range(2*n):
		for j in range(2*n):
			value = 1 
			if i < n:
				value += 2*i
			else:
				value += 2*(2*n-i-1)
			if j < n:
				value += 2*j
			else:
				value += 2*(2*n-j-1)
			if value >= 2*n:
				print(' ', end='')
			else:
				print(value, end='')
		print()