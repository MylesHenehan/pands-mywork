# Program that prompts a user to guess a number. The program will tell the user if the number is too high or too low, until they guess it.

# Author: Myles Henehan

correctnumber = 6
guess = int(input("Guess a number: "))

while guess != correctnumber:
    if guess < correctnumber:
        print ("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: "))

print(f"Well done! The correct number was indeed {correctnumber}.")