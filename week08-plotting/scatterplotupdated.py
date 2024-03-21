# update to scatterplot.py which also show y = x2

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

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color="r")
plt.show()
