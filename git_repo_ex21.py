# ex.21
# Create a program that reads 5 numbers and find the average of these numbers

# Create a program that:
# * Reads the 5 numbers you want
# * Calculates the average of these numbers
# * Input example: 4, 6, 1, 4, 9
# * Ouput: "the average is 4.8"

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
number4 = int(input("Enter fourth number: "))
number5 = int(input("Enter fifth number: "))

avg = sum([number1, number2, number3, number4, number5]) / 5

print(f"The average is {avg}")
