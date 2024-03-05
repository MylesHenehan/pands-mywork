# program that reads in and stores a student name and a list of their courses and grades, then prints out her data
# Author: Myles Henehan

studentname = input("Please enter your name: ")
modules = []

modulename = input("Please enter the module name: ")
modulegrade = input("Please enter the module grade: ")

while modulename != 0:
    modules = modules.append(modulename)

student = {
    "name" : studentname,
    "modules" : [
        {
            "coursename" : modulename,
            "grade" : modulegrade
        },
        {
            "coursename" : "History",
            "grade" : 99
        }
    ]
}

print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["coursename"], module["grade"]))