#reads in a student's name

#Author: Myles Henehan

students = []

def readmodules():
    modules = []
    modulename = input("\nEnter the first module name (blank to quit):").strip()

    while modulename != "":
        module = {}
        module["name"] = modulename

        module["grade"] = int(input("\t\tEnter Grade: "))
        modules.append(module)

        modulename = input("Enter next module name (blank to quit):").strip()

    return modules

def doadd(students):
    currentstudent = {}
    currentstudent["name"] = input("Enter name: ")
    currentstudent["modules"] = readmodules()
    students.append(currentstudent)

doadd(students)

doadd(students)
print(students)


def displaymodules (modules):
    print("\tName \tGrade")
    for module in modules:
        print(f"\t{ module["name"]} \t{ module["grade"]}")

def doview(students):
    for currentstudent in students:
        print(currentstudent["name"])
        displaymodules (currentstudent ["modules"]);