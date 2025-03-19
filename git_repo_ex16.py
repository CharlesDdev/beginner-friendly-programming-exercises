# ex.16
# A fast food chain has these meals

# | Meal | Price  |
# |---------|--------------|
# | Burger | 5$ |
# | Pizza | 3$ |
# | Hot Dog | 1,5$ |

# Create a program that:
# * Reads the meal the customer wants
# * Prints the cost of the meal
# * Input example: "Hot Dog"
# * Output: "Hot Dog 1,50$"

def meal_price(meal):
    if meal == "burger":
        return "Burger $5.00"
    elif meal == "pizza":
        return "Pizza $3.00"
    elif meal == "hot dog":
        return "Hot Dog 1.50$"
customer_meal_order = input("What meal would you like to order? ")
print(meal_price(customer_meal_order))
