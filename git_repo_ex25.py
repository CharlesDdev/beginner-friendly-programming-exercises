# ex.25
# You start flipping a coin,
# count and print how many times the result was head or tails until you enter the word "stop".
# Then find and print the percentage of how many head or tails was the result.

# Create a program that:
# * Reads if the flipped coin was head or tails
# * If the value is "stop", print proper message and quit program
# * While value not "stop", count the result
# * Print the proper message
# * Calculates the percentage of head and tails
# * Prints the proper message
# * Input: "head", "tails", "tails", "tails", "head", "head", "tails", "tails", "tails", "head"
# * Ouput: "Head won 4 times and tails won 6 times"
# * Output: "40% Head, 60% Tails"

flipped_coin = input("Enter heads or tails: ")
head_count = 0
tails_count = 0
head_count_percentage = 0
tails_count_percentage = 0
sum_of_flips = head_count + tails_count

if flipped_coin == "heads":
    head_count += 1
    head_count_percentage = head_count / sum_of_flips * 100
elif flipped_coin == "tails":
    tails_count += 1
    tails_count_percentage = tails_count / sum_of_flips * 100
elif flipped_coin == "stop":
    print("STOP")
elif head_count > tails_count:
    print(f"Heads won {head_count} times and tails won {tails_count} times")
    print(f"{head_count_percentage}%, {tails_count_percentage}%")
