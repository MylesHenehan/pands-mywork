# Add a legend, title and axis labels to the plot in scatterplotupdated

# Author: Myles Henehan

import numpy as np
import matplotlib.pyplot as plt

minsal = 20000
maxsal = 80000
numberofentries = 10

np.random.seed(1)
salaries = np.random.randint(minsal, maxsal, numberofentries)
ages = np.random.randint(low=21, high=65, size=numberofentries)
plt.scatter(ages, salaries, label = "salaries")

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color="r", label = "x-squared")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("Age")
plt.legend() 
#plt.show()
plt.savefig('prettier-plot.png') 