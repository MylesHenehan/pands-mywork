# program reads in a string and strips any leading or trailing spaces
# program also converts the string to lowercase
# program also outputs the length of the input and output strings

#Author: Myles Henehan

inputstring = input("Please enter a string: ")
normalisedstring = inputstring.strip().lower()

lengthofinputstring = len(inputstring)
lengthofnormalisedstring = len(normalisedstring)

print(f"That string normalised is {normalisedstring}")
print(f"We reduced the length of the string from {lengthofinputstring} to {lengthofnormalisedstring}.")
