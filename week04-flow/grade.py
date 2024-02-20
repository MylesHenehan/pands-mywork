# program that reads in a student's percentage mark and prints out corresponding grade
# Key: Under 40 (Fail), 40-49 (Pass), 50-59 (Merit 2), 60-69 (Merit 1), over 70 (Distinction)

# Author: Myles Henehan

percentage = float(input("Enter your grade: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100")
elif percentage < 40:
    print("Fail")
elif percentage < 50:
    print("Pass")
elif percentage < 60:
    print("Merit 2")
elif percentage < 70:
    print("Merit 1")
else:
    print("Distinction")
