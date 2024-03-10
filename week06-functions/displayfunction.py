# function that prints out a menu of commands we can perform (add, view, quit)
# returns the command we chose

# Author: Myles Henehan

def displaymenu ():
    print("What would you like to do?")
    print("\t (a) Add new students")
    print("\t (b) View students")
    print("\t (c) Quit")
    choice = input("Type one letter (a, v, q)\n")

    return choice

choice = displaymenu()
print(f"you chose {choice}")
