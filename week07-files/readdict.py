#  function that will read in a dict object from file
# Author: MH

import json
FILENAME = "testdict.json"

def readdict(): # will throw an error if the file does not exist
    with open(FILENAME) as f:
        return json.load(f)

somedict = readdict()
print(somedict)