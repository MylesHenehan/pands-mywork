#  function that will store a simple Dict to a file as JSON
# Author: Myles Henehan

import json # code begins by importing the json module, which provides functions for encoding and decoding JSON data.
FILENAME = "testdict.json" # Defining Constants: The code defines a constant FILENAME with the value "testdict.json". This constant specifies the name of the JSON file where the dictionary will be stored.
sample = dict(Name = "Fred", age = "31", grades = [1, 34, 55]) # Creating a Sample Dictionary: The code creates a sample dictionary named sample, which contains some key-value pairs. The dictionary includes keys such as 'name', 'age', and 'grades', with corresponding values.

def writedict(obj): # creates a function which takes an object as input...
    with open(FILENAME, "wt") as f: # opens the file in write mode ('wt')
        json.dump(obj, f) #  uses json.dump() to serialize the object (obj) to JSON format and write it to the file.

writedict(sample)

# Testing the writeDict() Function: The code tests the writeDict() function by calling it with the sample dictionary as the argument.
# This writes the contents of the sample dictionary to the JSON file specified by FILENAME.
