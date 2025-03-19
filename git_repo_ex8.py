# ex.8
# The exercise is almost identical to a previous exercise with a minor change.
# In a company the monthly salary of an employee is calculated by minimum wage 400$ per month,
# plus 20$ multiply by the employment years, plus 30$ for each employee kid,
# plus 100$ if the employee didn't miss 1 day of work.

# Create a program that:
# * Reads the employment years
# * Reads the number of each employee kids
# * Prints the total amount the employee must take
# * Output: "The total amount is 660$, 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids + 100$ for not missing a day at work"

years_employed = int(input("Enter the number of years employed: "))
number_of_children = int(input("Enter the number of children: "))

monthly_salary = 400 + (20 * years_employed) + (30 * number_of_children) + 100

print(f"The total amount is ${monthly_salary}. $400 minimum wage + ${20 * years_employed} for {years_employed} years experience + ${30 * number_of_children} for {number_of_children} kids + $100 for not missing a day at work")
