# Program that keeps reading a number until the user enters a 0. It will then read them out, along with the average.

# Author: Myles Henehan

numbers = []
number = int(input("Enter a number (press 0 to quit): "))

while number!= 0:
    numbers.append(number)
    number = int(input("Enter a number (press 0 to quit): "))

for value in numbers:
    print(value)

average = float(sum(numbers) / len(numbers))
print(f"The average is {average}")