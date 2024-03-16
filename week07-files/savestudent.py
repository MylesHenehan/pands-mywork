# using displaymenu prorgram from last week, but add another menu item called Save
#Author: MH

import json
FILENAME = "studentdata.json"

def displaymenu ():
    print("What would you like to do?")
    print("\t (a) Add new students")
    print("\t (v) View students")
    print("\t (s) Save student")
    print('\t (l) Load student data')
    print("\t (q) Quit")
    choice = input("Type one letter (a, v, s, l, q)\n")
    return choice

def doadd(students):
    currentstudent = {}
    currentstudent["name"] = input("Enter name: ")
    currentstudent["modules"] = readmodules()
    students.append(currentstudent)

def readmodules():
    modules = []
    modulename = input("\nEnter the first module name (blank to quit): ").strip()
    while modulename != "":
        module = {}
        module["name"] = modulename
        module["grade"] = int(input("\t\tEnter Grade: "))
        modules.append(module)
        modulename = input("Enter next module name (blank to quit): ").strip()
    return modules

def displaymodules (modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{ module['name']} \t{ module['grade']}")

def doview(students):
    for currentstudent in students:
        print(currentstudent["name"])
        displaymodules (currentstudent ["modules"]);

def dosave(students):
    with open(FILENAME, "wt") as f:
        json.dump(students, f)

    print("Students saved")

def doload(students):
    with open(FILENAME) as f:
        return json.load(f)

#mainprogram:
students = []
choice = displaymenu()
while choice != "q":
    if choice == "a":
        doadd(students)
    elif choice == "v":
        doview(students)
    elif choice == 's':
        dosave(students) 
    elif choice == "l":
        students = doload(students)
        print(students)
    elif choice != "q":
        print("\n\nPlease choose either a, v, s, l or q")
    choice = displaymenu()