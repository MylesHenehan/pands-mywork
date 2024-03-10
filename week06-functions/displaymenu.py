# function that prints out a menu of commands we can perform (add, view, quit)
# returns the command we chose
# continues displaying the menu until we choose q

# Author: Myles Henehan

def displaymenu ():
    print("What would you like to do?")
    print("\t (a) Add new students")
    print("\t (b) View students")
    print("\t (c) Quit")
    choice = input("Type one letter (a, v, q)\n")
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

#mainprogram:
students = []
choice = displaymenu()
while choice != "q":
    if choice == "a":
        doadd(students)
    elif choice == "v":
        doview(students)
    elif choice != "q":
        print("\n\nPlease choose either a, v, or q")
    choice = displaymenu()
