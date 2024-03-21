# program that makes a list called ages that has the same number random values as salaries (range:21 to 65).
# Make scatter plot of this data. 

# Author: Myles Henehan

import numpy as np
import matplotlib.pyplot as plt

minsal = 20000
maxsal = 80000
numberofentries = 10

np.random.seed(1)
salaries = np.random.randint(minsal, maxsal, numberofentries)

ages = np.random.randint(low=21, high=65, size=numberofentries)

plt.scatter(ages, salaries)
plt.show()