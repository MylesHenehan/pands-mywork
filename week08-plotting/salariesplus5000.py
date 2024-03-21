# Modifies salaries.py to add 5000 to each number
# Author: Myles Henehan

import numpy as np

minsal = 20000
maxsal = 80000
numberofentries = 10

np.random.seed(1)
salaries = np.random.randint(minsal, maxsal, numberofentries)

salariesplus = salaries + 5000
print(salariesplus)