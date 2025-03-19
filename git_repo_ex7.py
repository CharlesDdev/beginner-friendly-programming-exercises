# ex.7
# In a company the monthly salary of an employee is calculated by: the minimum wage 400$ per month,
# plus 20$ multiplied by the number of years employed, plus 30$ for each child they have.

# Create a program that:
# 1) Reads the number of years employed
# 2) Reads the number of children the employee has
# 3) Prints the total amount of salary the employee makes

# * Output: "The total amount is 560$. 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"

years_employed = int(input("Enter the number of years employed: "))
number_of_children = int(input("Enter the number of children: "))
monthly_salary = 400 + (20 * years_employed) + (30 * number_of_children)

print(f"The total amount is ${monthly_salary}. $400 minimum wage + ${20 * years_employed} for {years_employed} years experience + ${30 * number_of_children} for {number_of_children} kids")
