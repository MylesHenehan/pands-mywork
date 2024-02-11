# Program which prints out a random fruit name using a tuple
# Author Myles Henehan

import random
fruits = ('banana', 'apple', 'orange', 'pear', 'grapefruit', 'peach')
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print('A random fruit is {}'.format(fruit))