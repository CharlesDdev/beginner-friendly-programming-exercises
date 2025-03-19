# ex.10
# Create a program that prints the last digit of a given integer

# Create a program that:
# 1) Reads the integer
# 2) Prints the last digit

# Warning! Do not use the programming language MAGIC. After you complete the exercise feel free to do so.

# Warning! Don't try to convert the number into string etc.

# Warning! For this problem it's ok after spending some time to look for the solution.

last_digit_number = int(input("Enter a number: ")) # reads the integer
last_digit = abs(last_digit_number) % 10 # calculates the last digit by dividing with 10 and taking the remainder
print(f"The last digit of the number you entered is: {last_digit}")
