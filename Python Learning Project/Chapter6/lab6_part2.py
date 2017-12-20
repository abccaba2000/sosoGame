n = int(input('n= '))
if n >= 2:
	'''
	for i in range(n):
		print('o',end='')
	print()
	for i in range(n-2):
		print('o', end='')
		for j in range(n-2):
			print(' ', end='')
		print('o')
	for i in range(n):
		print('o',end='')
	'''
	a = 'o'*n+'\n'
	b = 'o'+' '*(n-2)+'o'+'\n'
	print(a+b*(n-2)+a)