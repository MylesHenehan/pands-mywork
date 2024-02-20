# Program that prompts a user to guess a number. The program keeps prompting until the user gets the right one.

# Author: Myles Henehan

correctnumber = 6
guess = int(input("Guess a number: "))

while guess != correctnumber:
    print("Incorrect")
    guess = int(input("Please guess again: "))

print(f"Well done! The correct number was indeed {correctnumber}.")