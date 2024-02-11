# Program to divide one number by another and give a remainder
# Author: Myles Henehan

x = int(input("Enter the first number: "))
y = int(input("Enter a second number: "))
answer = x // y
remainder = x % y
print('{} divided by {} is {}, with {} remaining' .format(x, y, answer, remainder))