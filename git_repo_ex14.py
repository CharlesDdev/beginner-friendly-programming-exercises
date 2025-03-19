# ex.14
# You want to buy something from Amazon.
# The seller charges different prices for shipping cost based on location.
# For US it's 5$ for Europe it's 7$ for Canada it's 3$ for other places it's 9$

# Create a program that:
# * Reads the cost of the product
# * Reads your location
# * Print the amount of money you have to pay
# * Ouput: "You have to pay 23$, 20$ for the product and 3$ for shipping cost"


cost_of_item = int(input("Enter the cost of the item:"))
location = input("Enter location for delivery (US/EU/CAN/OTHER):")

print(f"You have to pay ${cost_of_item + (5 if location == 'US' else 7 if location == 'EU' else 3 if location == 'CAN' else 9)}, ${cost_of_item} for the product and ${(5 if location == 'US' else 7 if location == 'EU' else 3 if location == 'CAN' else 9)} for shipping cost")
