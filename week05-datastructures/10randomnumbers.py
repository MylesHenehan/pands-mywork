# program that puts 10 random numbers into a queue(list), and then outputs all the values in the queue
# program then takes the numbers from the queue one at a time, prints them and the current numbers still in the queue

#Author: Myles Henehan 

import random
#importing the random module for use
queue = []
#defining queue as a list
numberofnumbers = 10
#defining the number of numbers we want in the list
rangeto = 100
#defining the highest number we want

for n in range(0,numberofnumbers):
    queue.append(random.randint(0,rangeto))
# in other words, until there are 10 numbers, add a random integer up to 100

print(f"The queue is {queue}")
#print the queue which has just been added to

while len(queue) != 0:
    currentnumber = queue.pop(0)
    print(f"current number is {currentnumber} and the queue is {queue}")
# the command pop(0) takes the first element out of a list
# in other words, so long as there are still numbers in the queue, print the first number and give the rest of the queue.

print("The queue is now empty")
# when all numbers are gone, tell the user that the queue is empty

