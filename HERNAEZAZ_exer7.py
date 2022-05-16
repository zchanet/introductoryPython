# this program serves the purpose of indicating how well I understood incorporating recursive method/s in a problem-solving process
# There will be two lists to be used since lists can actually embody one-dimensional vectors.

length_of_list = int(input("How many items are to be placed in a list containing numerical values? "))
list1 = []
list2 = []

for item1 in range(length_of_list):
    item1 = input("Enter number for list1: ")
    if "." in item1:
        item1 = float(item1)
    else:
        item1 = int(item1)
    list1.append(item1)

print("\n...Enter contents for the second list...\n")
for item2 in range(length_of_list):
    item2 = input("Enter number for list2: ")
    if "." in item2:
        item2 = float(item2)
    else:
        item2 = int(item2)
    list2.append(item2)

# Keep in mind that recursion incorporates the process of breaking down the problem into smaller pieces!
augends = list1.copy()
addends = list2.copy()
addition_results = []

def addVectors(augends, addends):
    if len(augends) == len(addends) == 0:
        return addition_results
    else:
        augend = augends.pop(0)
        addend = addends.pop(0)
        addition_results.append(augend + addend)
        return addVectors(augends, addends)

minuends = list1.copy()
subtrahends = list2.copy()
subtraction_results = []

def subtractVectors(minuends, subtrahends):
    if len(minuends) == len(subtrahends) == 0:
        return subtraction_results
    else:
        minuend = minuends.pop(0)
        subtrahend = subtrahends.pop(0)
        subtraction_results.append(minuend - subtrahend)
        return subtractVectors(minuends, subtrahends)

def get_sum_of_list1(list1):
    if len(list1) == 0:
        return 0
    else:
        return list1[0] + get_sum_of_list1(list1[1:])

def get_sum_of_list2(list2):
    if len(list2) == 0:
        return 0
    else:
        return list2[0] + get_sum_of_list2(list2[1:])

def getSummation():
    print("Which list do you want to add each element altogether?\n\t[1] List1\n\t[2] List2\n\t[3] Go Back to Menu")
    choice = input("Choice: ")
    while True:
        if choice == "1":
            print(f"The summation of list1 is: {get_sum_of_list1(list1)}")
            break
        elif choice == "2":
            print(f"The summation of list2 is: {get_sum_of_list2(list2)}")
            break
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
            break

def showMenu():
    print("\n[1] Add Vectors")
    print("[2] Subtract Vectors")
    print("[3] Get summation")
    print("[4] Exit")

    choice = input("Choice: ")
    return choice

while True:
    choice = showMenu()

    if choice == "1":
        print(f"The sum of two vectors is {addVectors(augends, addends)}")
    elif choice == "2":
        print(f"The difference of two vectors is {subtractVectors(minuends, subtrahends)}")
    elif choice == "3":
        getSummation()
    elif choice == "4":
        print("\nThanks for using this program!")
        break
    else:
        print("Input wasn't among the choices. Please try again.")