# ex.15
# A cell phone company has the following billing policy


# |  | Fixed cost 25$  |
# |---------|--------------|
# | Call duration(in seconds)| Charge($/per second)|
# | 1-500 | 0,01 |
# | 501-800 | 0,008 |
# | 801+ | 0,005 |

# Create a program that:
# * Reads how many seconds was the calls duration
# * Calculates the monthly bill for the subscriber
# * Prints the total amount
# * Output: "total amount: 48$"

#### Notice that that the charge for the first 500 seconds it's 0,01$ then for the next 501 to 800 seconds it's 0,008 and then it's 0,005$

how_many_seconds = int(input("How many seconds was the call duration? "))
if how_many_seconds <= 500:
    monthly_bill = how_many_seconds * 0.01
elif how_many_seconds > 500 and how_many_seconds <= 800:
    monthly_bill = 500 * 0.01 + (how_many_seconds - 500) * 0.008 # not quite sure here if it's correct

print(f"Total amount: ${monthly_bill}")
