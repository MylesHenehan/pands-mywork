# function that reads in a number from a file that already exists (count.txt)
# Author: Myles Henehan

FILENAME = "count.txt"

def readnumber(): # define a function which...
    with open(FILENAME) as f: #opens a file, henceforth referring to it as f
        num = int(f.read()) # reads the data in the file and converts it to an integer - designating it "num"
        return num # returns that num
    
#let's test
    
num = readnumber() # call the function
print(num) # print out the output
