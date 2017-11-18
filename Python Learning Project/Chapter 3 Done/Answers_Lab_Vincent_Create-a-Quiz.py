right_answer_count = 0
question_count = 0

question_count += 1
ans_1 = input("What is \"2 - 1\" ? ")
if ans_1 == "1" :
	print("You're right!")
	right_answer_count += 1
else :
	print("See you are sosoing.")


question_count += 1
print()
ans_2 = input("What is the first name of Dehan ? ")
if ans_2.lower() == "wang" :
	print("You hen bon!")
	right_answer_count += 1
else :
	print("You hen fay.")


question_count += 1
print()
print("A. Grass")
print("B. Psychic")
print("C. Dragon")
print("D. Normal")
ans_3 =  input("What is not the attribute of an Exeggutor? ")
if ans_3.upper() == "D":
	print("How do you know this...")
	right_answer_count += 1
elif ans_3.upper() == "A" or ans_3.upper() == "B" or ans_3.upper() == "C" :
	print("Wrong...")
else :
	print("No this answer...")


question_count += 1
print()
ans_4 = input("Are you a sosoker? ")
if ans_4.lower() == "yes" :
	print("I got it!")
	right_answer_count += 1
else :
	print("Lier!")


question_count += 1
print()
ans_5 = input("Is python easy to learn? ")
if ans_5.lower() == "no" :
	print("I think so..")
	right_answer_count += 1
else :
	print("You can come here and soso!")


print()
print("Questions : ", question_count)
print("Points : ", right_answer_count)
print("Score Rate : ", right_answer_count/question_count*100, "%")