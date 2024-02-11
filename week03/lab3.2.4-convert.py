# takes in a float amount of dollars and returns that absolute amount in cent
# Author: Myles Henehan

numbertobeconverted = float(input("Please input the number in dollars and cents: "))
absolutenum = abs(numbertobeconverted)
absolutecents = absolutenum * 100
print("That amount in cent is {}" .format(absolutecents))