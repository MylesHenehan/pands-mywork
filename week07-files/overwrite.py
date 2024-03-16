#  function that takes in a number and overwrites a file with that number (count.txt)
# Author: Myles Henehan

FILENAME = "count.txt"

def writenumber(num): # define the function which...
    with open(FILENAME, "wt") as f: # ...opens the file in write mode, calling it "f"
      f.write(str(num)) # writes this number in as a string
    
# let's test
writenumber(3)

# "count.txt" now contains the value 3