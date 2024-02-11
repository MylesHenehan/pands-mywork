# Program that prints out a random number between 1 and 10
# Author: Myles Henehan

import random
startofrange = int(input("First number in the range: "))
endofrange = int(input("Last number in the range: "))
number = random.randint (startofrange, endofrange)

print("Here is a random number: {}" .format(number))