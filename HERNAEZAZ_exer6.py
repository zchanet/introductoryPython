'''

This application serves the purpose of holding the records of our valued fitness club members here at 'Karmic Fit Centre'
where the consequences of your bodily-kinesthetic actions will certainly yield desired results.

Author: Hernaez, Ariane Zchanet Y.

'''

# This program is a continuation of Exercise 5 about dictionaries along with the integration of saving and loading records of a file.

def showMenu():
    print("\nOptions: ")
    print("[1] Add a member")
    print("[2] View a member record")
    print("[3] View all members")
    print("[4] Edit a member record")
    print("[5] Delete a member record")
    print("[6] Delete all member records")
    #Include two more options that can save and load to/from a file
    print("[7] Save a file")
    print("[8] Load from file")
    print("[0] Exit")

    choice = input("Choice: ")
    return choice

memberRecords = {}
memberData = {}

def addMember():
    name = input("Enter name: ")
    weight = float(input("Enter weight (kg): "))
    height = int(input("Enter height (cm): "))
    BMI = weight/((height*0.01)**2)
    type = ""
    if BMI < 18.5:
        type = "Underweight"
    elif BMI >= 18.5 and BMI < 24.9:
        type = "Normal"
    elif BMI >= 25 and BMI < 29.9:
        type = "Overweight"
    else:
        type = "Obese"
    BMI = round(BMI, 1)
    print("BMI is", BMI)
    print("Type is", type)
    dataList = []
    dataList.append(name)
    dataList.append(weight)
    dataList.append(height)
    dataList.append(BMI)
    dataList.append(type)
    counter = 1
    if len(memberRecords) == 0:
        key = "M" + str(counter).zfill(3)
        memberData[key] = dataList
        memberRecords[counter] = memberData
    else:
        while counter <= next(reversed(memberRecords.keys())):
            counter += 1
        key = "M" + str(counter).zfill(3)
        memberData[key] = dataList
        memberRecords[counter] = memberData

def viewOne():
    memberID = input("Enter member ID: ")
    if memberID in memberData.keys():
        print("\n======Member Information======")
        print("(" + memberID + ") ", end="")
        print(memberData[memberID][0], end="")
        print("", memberData[memberID][1], "kg", end="")
        print("", memberData[memberID][2], "cm", end="")
        print(" (BMI: " + str(memberData[memberID][3]) + "; " + memberData[memberID][4] + ")")
    else:
        print("The record does not exist.")

def viewAll():
    print("\n======List of members======")
    counter = 1
    for k in memberData:
        print(str(counter) + ". ", end="")
        print("(" + k + ") ", end="")
        print(memberData[k][0], end="")
        print("", memberData[k][1], "kg", end="")
        print("", memberData[k][2], "cm", end="")
        print(" (BMI: " + str(memberData[k][3]) + "; " + memberData[k][4] + ")")
        counter = counter + 1

def editData():
    memberID = input("Enter the member ID of a record you wish to edit: ")
    if memberID in memberData.keys():
        while True:
            print("\nWhich among these two do you want to edit in case previous input is incorrect:")
            print("[1] Name\n[2] Weight\n[3] None")
            choice = input("Enter your choice: ")
            if choice == "1":
                editedName = input("Enter accurate datum for their name: ")
                memberData[memberID][0] = editedName
            elif choice == "2":
                editedWeight = float(input("Enter accurate datum for their weight: "))
                memberData[memberID][1] = editedWeight
                memberData[memberID][3] = editedWeight / ((memberData[memberID][2] * 0.01) ** 2)
                if memberData[memberID][3] < 18.5:
                    memberData[memberID][4] = "Underweight"
                elif memberData[memberID][3] >= 18.5 and memberData[memberID][3] < 24.9:
                    memberData[memberID][4] = "Normal"
                elif memberData[memberID][3] >= 25 and memberData[memberID][3] < 29.9:
                    memberData[memberID][4] = "Overweight"
                else:
                    memberData[memberID][4] = "Obese"
                memberData[memberID][3] = round(memberData[memberID][3], 1)
            elif choice == "3":
                break
            else:
                print("Input wasn't among the choices. Please try again.")
    else:
        print("The record does not exist.")

def deleteOne():
    memberID = input("Enter member ID: ")
    if memberID in memberData.keys():
        del memberData[memberID]
        recordKey = int(memberID[1:])
        del memberRecords[recordKey]
        print("Member", memberID, "successfully deleted.")
    else:
        print("The record does not exist.")

def deleteAll():
    memberRecords.clear()
    memberData.clear()
    print("All entries successfully deleted.")

def saveToFile():
    fileHandle = open("records.txt", "w")
    entry = 0
    for k in memberData:
        for element in k:
            memberName = str(memberData[k][0])
            memberWeight = str(memberData[k][1])
            memberHeight = str(memberData[k][2])
            memberBMI = str(memberData[k][3])
            memberType = str(memberData[k][4])
        fileHandle.write(k + "_" + memberName + "_" + memberWeight + "_" + memberHeight + "_" + memberBMI + "_" + memberType + "\n")
        entry += 1
    fileHandle.close()
    print("Successfully saved", entry, "entries to file.")

#Before, the function for saving every data entry performs by storing data in a variable that represents a file
#The next function will then access that file in order to take in its contents into the two essential dictionaries

def loadFromFile():
    fileHandle = open("records.txt", "r")
    memberRecords.clear()
    memberData.clear()
    entry = 0
    for line in fileHandle:
        data = line[:-1].split("_")
        memberID = data.pop(0)
        finalWeight = float(data[1])
        finalHeight = int(data[2])
        finalBMI = float(data[3])
        data[1] = finalWeight
        data[2] = finalHeight
        data[3] = finalBMI
        counter = int(memberID[1:])
        memberData[memberID] = data
        memberRecords[counter] = memberData
        entry += 1
    fileHandle.close()
    print("Successfully loaded", entry, "entries from file.")

print("Welcome to Karmic Fit Centre!")

while True:
    choice = showMenu()

    if choice == "1":
        addMember()
    elif choice == "2":
        viewOne()
    elif choice == "3":
        viewAll()
    elif choice == "4":
        editData()
    elif choice == "5":
        deleteOne()
    elif choice == "6":
        deleteAll()
    # add the two functions to execute what is being tasked to do
    elif choice == "7":
        saveToFile()
    elif choice == "8":
        loadFromFile()
    elif choice == "0":
        print("\nThank you for using this program!")
        break
    else:
        print("\nInput wasn't among the choices. Please try again.")