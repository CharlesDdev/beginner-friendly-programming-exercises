# ex.3

# You've bought a Bitcoin and now it's on the rise!!!

# Create a program that:

# Reads the value of the bitcoin at the time of purchase
# Reads the percentage of increase (or decrease)
# Prints the total value of your bitcoin
# Prints the increase or decrease value
# Example: bitcoin_value = 10000, bitcoin_increase = 10
# Output: total_bitcoin_value = 11000, bitcoin_increase_value = 1000


value_of_bitcoin = int(input("Enter the value of the bitcoin at the time of purchase: "))
bitcoin_percentage_of_increase_decrease = int(input("Enter the percentage of increase or decrease: "))
total_value_of_bitcoin = int(value_of_bitcoin + (value_of_bitcoin * (bitcoin_percentage_of_increase_decrease / 100)))
bitcoin_increase_value = bitcoin_percentage_of_increase_decrease * 100

print(f"total_bitcoin_value = {total_value_of_bitcoin}, bitcoin_increase_value = {bitcoin_increase_value}")
