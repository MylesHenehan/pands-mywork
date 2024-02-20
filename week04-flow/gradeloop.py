# program that reads in a student's percentage mark and prints out corresponding grade
# Key: Under 40 (Fail), 40-49 (Pass), 50-59 (Merit 2), 60-69 (Merit 1), over 70 (Distinction)

# Author: Myles Henehan

percentage = float(input("Enter your grade: "))

while percentage != -1:
    if percentage > 100:
        print("Please enter a percentage under 100")
    if percentage < 40:
        print("Fail")
    elif percentage < 50:
        print("Pass")
    elif percentage < 60:
        print("Merit 2")
    elif percentage < 70:
        print("Merit 1")
    elif percentage < 101:
        print("Distinction")
    percentage = float(input("Enter your grade: "))
   
print("Marks complete")

