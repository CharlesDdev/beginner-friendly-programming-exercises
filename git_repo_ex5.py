# ex.5
# #You are interested in buying crypto-currencies. You want to check the current amount of money you have and see how many coins you can buy in Bitcoin, Ethereum, and Litecoin.

# Create a program that:

# Reads the total amount of money you have
# Reads the price of Bitcoin, Ethereum, and Litecoin
# Prints the amount of Bitcoin, Ethereum, and Litecoin you can buy
# Example: money = 100, bitcoin_price = 50, ethereum_price = 25, litecoin_price = 10
# Output: "With 100$ you can buy: 2 Bitcoins, 4 Ethereum, and 10 Litecoins"
# (Warning! Τhe prices are made up for exercise purposes)
#

tot_amount_of_money = int(input("Enter how much money you have:"))
price_of_bitcoin = int(input("Enter price of Bitcoin:"))
price_of_ethereum = int(input("Enter price of Ethereum:"))
price_of_litecoin = int(input("Enter price of Litecoin:"))

number_of_bitcoin_you_can_buy = int((tot_amount_of_money/price_of_bitcoin))
number_of_ethereum_you_can_buy = int((tot_amount_of_money/price_of_ethereum))
number_of_litecoin_you_can_buy = int((tot_amount_of_money/price_of_litecoin))

print(f"With ${tot_amount_of_money} you can buy: {number_of_bitcoin_you_can_buy} Bitcoins, {number_of_ethereum_you_can_buy} Ethereum, and {number_of_litecoin_you_can_buy} Litecoins")#number of ethereum a
