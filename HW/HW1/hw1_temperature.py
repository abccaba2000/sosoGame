print("This program translate the temperature in Fahrenheit to Celsius.")
 
# Get the temperature in Fahrenheit from user
fah = input("Enter temperature in Fahrenheit: ")

# Convert text entered to a floating point number
fah = float(fah)
 
# Calculate and print the answer
cel = (fah - 32) * 5 / 9
print("The temperature in Celsius:", cel)