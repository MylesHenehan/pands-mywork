# program that plots a histogram of the salaries from salaries.py
# Author: Myles Henehan

import numpy as np
import matplotlib.pyplot as plt

minsal = 20000
maxsal = 80000
numberofentries = 10

np.random.seed(1)
salaries = np.random.randint(minsal, maxsal, numberofentries)


plt.hist(salaries)
plt.show()