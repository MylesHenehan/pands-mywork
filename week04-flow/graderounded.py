# program similar to grade.py, but modified to allow for grades to be rounded
# Key: Under 40 (Fail), 40-49 (Pass), 50-59 (Merit 2), 60-69 (Merit 1), over 70 (Distinction)

# Author: Myles Henehan

percentage = float(input("Enter your grade: "))
roundedpercentage = round(percentage)

if roundedpercentage < 0 or roundedpercentage > 100:
    print("Please enter a number between 0 and 100")
elif roundedpercentage < 40:
    print("Fail")
elif roundedpercentage < 50:
    print("Pass")
elif roundedpercentage < 60:
    print("Merit 2")
elif roundedpercentage < 70:
    print("Merit 1")
else:
    print("Distinction")