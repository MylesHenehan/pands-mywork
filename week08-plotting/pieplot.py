# Program that has a list of counties (5+).  
# Some counties appear more than others. 
# Make a pie chart of the counties. 

import numpy as np
import matplotlib.pyplot as plt

possiblecounties = ["Galway", "Mayo", "Dublin", "Roscommon", "Sligo", "Donegal", "Cork"]

counties = np.random.choice(possiblecounties, p=[0.1, 0.3, 0.1, 0.12, 0.24, 0.1, 0.04], size=(100))

unique, counts = np.unique(counties, return_counts=True)

# print(unique) would show you the unique values in the counties list
# print(counts) would show you the number of each

plt.pie(counts, labels=unique)

plt.show()

plt.bar(unique, counts)

plt.show()
