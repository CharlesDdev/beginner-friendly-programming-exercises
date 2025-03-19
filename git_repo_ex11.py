# ex.11
# You have started working and you are wondering how many things you can buy with the money you've earned.
# A PS4 costs 200$, a Samsung phone 900$, a TV 500$, a game skin 9.99$

# Create a program:
# * Notice that you can't but half TV or 1/4 of PS4.
# * Reads how many hours you've worked
# * Reads your hourly income
# * Prints how many items you can buy
# * Output: "I can buy 4 PS4, 1 Samsung, 3 TV, 80 game skin"

how_many_hours_worked = int(input("How many hours you've worked: "))
hourly_income = float(input("Your hourly income: "))
price_of_ps4 = int(input("Price of PS4: "))
price_of_phone = int(input("Price of Samsung: "))
price_of_tv = int(input("Price of TV: "))
price_of_game_skin = float(input("Price of game skin: "))
income = how_many_hours_worked * hourly_income
how_many_ps4 = int(income // price_of_ps4)
how_many_phones = int(income // price_of_phone)
how_many_tv = int(income // price_of_tv)
how_many_game_skins = int(income // price_of_game_skin)
print(f"I can buy {how_many_ps4} PS4, {how_many_phones} Samsung, {how_many_tv} TV, {how_many_game_skins} game skins.")
