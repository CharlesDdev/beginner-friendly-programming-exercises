# ex.12
# You've consumed X amount of Mbps on Wikipedia and Y amount of Mbps on memes. The cost of visiting Wikipedia is 0,10$ per Mb
# and the cost for watching memes is 0,05$ per Mb. If total consumption  is more than 100$ print "Too much consumption".
# If watching meme consumption is greater than reading wikipedia consumption print "WOW MANY MEMES", "SUCH LOL"(in new line).

# Create a program that:
# * Reads X(wikipedia Mb consupmtion) and Y(watching meme Mb consumption)
# * Calculates the total consumption
# * If total consumption greater than 100$ print proper message
# * If watching meme consumption  is greater than reading wikipedia articles print proper messages

# Warning! For the greater meme consumption you will use one print statement and the output must be in seperate lines

meme_consumption = float(input("Enter the amount of memes consumed in Mb: "))
wikipedia_consumption = float(input("Enter the amount of Wikipedia consumed in Mb: "))
meme_cost = 0.05
wikipedia_cost = 0.10
total_meme_cost = float(meme_consumption * meme_cost)
total_wikipedia_cost = float(wikipedia_consumption * wikipedia_cost)
total_consumption = total_meme_cost + total_wikipedia_cost
if total_consumption > 100:
    print("Too much consumption")
elif total_meme_cost > total_wikipedia_cost:
    print("WOW MANY MEMES\nSUCH LOL")
else:
    print("Total consumption: ", total_consumption, "$")
    print("Total meme consumption: ", total_meme_cost, "$")
    print("Total wikipedia consumption: ", total_wikipedia_cost, "$")
