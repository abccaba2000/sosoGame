print("This program caculate your BMI!!")
 
# Get the height, weight  from user
height = input("How tall are you?(cm) ")
weight = input("How heavy are you?(kg) ")

# Convert text entered to a floating point number
height = float(height)
weight = float(weight)

#convert the value in centimrter to meter
height = height/100

# Calculate and print the answer
bmi = weight / ( height**2 )
print("Your BMI is:", bmi)