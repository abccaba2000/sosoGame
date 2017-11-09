print("Quiz Time!")
print("The following questions challenge how you are familiar with ...... Vincent's Blog!")

correct_n = 0
question_n = 5

acceptable = input("Do you consider this challenge acceptable ??!!!(yes/no)\n")

if acceptable == 'yes':

	print("\ntoo god la\n")
	n_authors = input("first question:\n\tHow many authors are there in Vincent's blog??\n")
	if n_authors == '3':
		print("\ntoo god la\n")
		correct_n += 1
	else:
		print("\nAre you sosoker?\n")
	
	article_1_2017 = input("next challenge:\n\tHow many articles are posted in January 2017?\n")
	if article_1_2017 == '2':
		print("\ntoo god la\n")
		correct_n += 1
	else:
		print("\nAre you sosoker?\n")
	
	print("I am a little tired:\n\tIn which poem the first sentence is \"Who is she?\"")
	print("\tA\tTo not-very-familiar-with-MRT You")
	print("\tB\tProfessor")
	print("\tC\tThe Bird Which Is Not Able To Crash The Ceiling")
	poem = input("\tD\tFill Back\n")
	
	if poem == 'D' or poem == 'd':
		print("\ntoo god la\n")
		correct_n += 1
	else:
		print("\nAre you sosoker?\n")	
	
	star_sign = input("\t What's the star sign of Vincent?\n")
	if star_sign == 'Taurus' or star_sign == 'taurus' or  star_sign == 'sosoker':
		print("\ntoo god la\n")
		correct_n += 1
	else:
		print("\nAre you sosoker?\n")

	ok = input("Just answer my last question ok?(ok/no)\n")
	if ok == 'ok':	
		instrument = input("\t According to the article \"Small Band Practice\" Which instrument the one who is working on experiments play?\n")
		if instrument == 'keyboard':
			print("\ntoo god la\n")
			correct_n += 1
		else:
			print("\nAre you sosoker?\n")
	else:
		correct_n -= 100
	
score = correct_n/question_n*100

print("\n\nyour score is ", score)