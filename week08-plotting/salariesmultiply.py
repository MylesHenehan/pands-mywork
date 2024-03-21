# Modifies salaries.py to add 5% to each number
# Author: Myles Henehan

import numpy as np

minsal = 20000
maxsal = 80000
numberofentries = 10

salaries = np.random.randint(minsal, maxsal, numberofentries)
print(salaries)

salariesplus5 = salaries * 1.05
newsalaries = salariesplus5.astype(int)
print(newsalaries)