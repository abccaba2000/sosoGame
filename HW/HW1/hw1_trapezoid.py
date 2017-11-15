print("This program caculate the area of a trapezoid.")
 
# Get the height, length of the bottom base, length of the top base from user
height = input("Enter the height of the trapezoid:")
l_bottom = input("Enter the length of the bottom base:")
l_top = input("Enter the length of the top base:")


# Convert text entered to a floating point number
height = float(height)
l_bottom = float(l_bottom)
l_top = float(l_top)
 
# Calculate and print the answer
area = (l_bottom + l_top)*height/2
print("The area is:", area)