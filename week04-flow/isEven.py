# program that reads in a number and tells the user if it's odd or even

# Author: Myles Henehan

number = int(input("Please enter an integer: "))

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
