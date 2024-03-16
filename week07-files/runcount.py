# uses two functions to count how many times the program has been run
# Author: Myles Henehan

FILENAME = "count.txt"

def readNumber():
    with open(FILENAME, "r") as f:  # Open file in read mode
        number = int(f.read())  # Read the content of the file and convert it to an integer
    return number

def writeNumber(number):
    with open(FILENAME, "wt") as f:  # Open file in write mode
        f.write(str(number))  # Write the string representation of the number to the file

# Main execution
num = readNumber()  # Read the current count from the file
num += 1  # Increment the count (can also be written as num = num + 1)
if num == 1:
    print(f"We have run this program once")
else:
    print(f'We have run this program {num} times')  # Print a message indicating the number of times the program has been run
writeNumber(num)  # Write the updated count to the file