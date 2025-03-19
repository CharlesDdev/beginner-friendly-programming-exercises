# ex.23
# Create a program that reads numbers and sum them until the user inputs a negative value

# Create a program that:
# * Reads numbers
# * Sum them
# * Prints the sum
# * Input example: 5, 9, 3, 0, 2, 0, 4, -7 **NOTE** you must input the numbers one by one
# * Output: "The sum is 23"

numbers = []
sum_of_numbers = 0
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    numbers.append(number)
    sum_of_numbers = sum(numbers)
    print(f"The sum is {sum_of_numbers}")
