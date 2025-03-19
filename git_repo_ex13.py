
# ex.13
# An internet cafe has 2 ways of charging. If the user is a member pays 2$/hour, Else the user pays 5$.
# Find if someone is a member or not and calculate the price based on how many hours the user spend.
# If the user is a member the tax is 10% else the tax is 20%.

# Create a program that:
# * Reads how many hours the user spend
# * Check if is a member
# * Add the proper tax fee
# * Print the total amount the user has to pay
# * Output: "The user is a member stayed 2 hours for 2$/hour plus the 10% the total amount is 4.4$"

how_many_hours = int(input("How many hours did you stay? "))
member_status = input("Are you a member? (yes/no) ")

if member_status == "yes":
    print(f"The user is a member. Stayed {how_many_hours} hours for $2 per hour + 10% tax. The total amount is ${how_many_hours * 2 * 1.1}")
else:
    print(f"The user is not a member. Stayed {how_many_hours} hours for $5 per hour + 20% tax. The total amount is ${how_many_hours * 5 * 1.2}")
