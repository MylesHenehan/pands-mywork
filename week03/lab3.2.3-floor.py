# Program takes in a float, outputs an int rounded down (floored)
# Author: Myles Henehan

import math

numbertobefloored = float(input("Enter a float: "))
floorednumber = math.floor(numbertobefloored)
print("{} floored is {}" .format(numbertobefloored, floorednumber))

#This program still ends up with a minus value?