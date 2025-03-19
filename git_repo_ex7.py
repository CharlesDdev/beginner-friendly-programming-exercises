# In a company the monthly salary of an employee is calculated by:
# the minimum wage 400$ per month, plus 20$ multiplied by the number of years employed,
# plus 30$ for each child they have.

# Create a program that:

# Reads the number of years employed
# Reads the number of children the employee has
# Prints the total amount of salary the employee makes
# Output: "The total amount is 560$.
# 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"
#

years_employed = input("How many years have you been employed: ")
number_of_kids = int(input("How many children do you have: "))


print(f"The total amount is ${total}.")
print(f"${min_wage} minimum wage + ${years_exp} for {years_employed} + ${money_for_kids} for {number_of_kids}")
