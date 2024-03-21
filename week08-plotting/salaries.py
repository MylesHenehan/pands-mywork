# Write a program that makes a list, called salaries, that has (say 10) random numbers (20000 – 80000). 
# Author: Myles Henehan

import numpy as np

minsal = 20000
maxsal = 80000
numberofentries = 10

salaries = np.random.randint(minsal, maxsal, numberofentries)

print(salaries)