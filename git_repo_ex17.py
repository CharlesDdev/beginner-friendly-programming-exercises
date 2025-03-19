# ex.17
# Create a program that:
# * Calculates the sum of 1+2+3+4...+98+99
# * Prints the sum of 1+2+3+4...+98+99
# * Output: "The sum is 4950"

sum_of_99 = 0
for i in range(1, 100):
    sum_of_99 += i
    print(f"The sum is {sum_of_99}")
