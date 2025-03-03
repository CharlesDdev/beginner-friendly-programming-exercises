# ex.6

# You are interested in buying a new laptop. You check the price and you see that the price is 300$ without the 10% tax.

# Create a program that:

# Reads the price of the laptop
# Reads the tax percentage
# Prints the total amount
# Output: "The total price of the laptop is 330$"


price_of_laptop = int(input("Enter the price of the laptop:"))
tax_percentage = int(input("Enter the tax percentage:"))

print(f"The total price of the laptop is ${price_of_laptop + int((price_of_laptop * tax_percentage / 100))}")
