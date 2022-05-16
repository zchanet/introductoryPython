# Application of learnings about data structures and sequence data types in Python, specifically lists and strings.
# This program implements the game titled "6K’s of relationship" (Filipino version)

print('Want to know what relationship two persons have?\nWell this is just the right program for you!\nIt tells you whether they are "Kaibigan", "Kapuso", "Kaaway", "Kasal", "Kilig" (crush), or "Kapatid" based on the number of distinctive letters left.')
#STEP 1
name_1 = input("\nPlayer 1 name: ")
name_2 = input("Player 2 name: ")
name_1 = name_1.replace(" ", "")
name_2 = name_2.replace(" ", "")
#STEP 2
def get_unique(x, y):
    global name_1
    global name_2
    player_1 = ""
    player_2 = ""
    for i in name_1.lower():
        if i not in name_2.lower():
            player_1 = player_1 + i
    for j in name_2.lower():
        if j not in name_1.lower():
            player_2 = player_2 + j
#STEP 3
    total_characters = sum(len(c) for c in player_1 + player_2)
    return total_characters
counted_characters = get_unique(name_1, name_2)
#STEP 4-5
K_list = ["K1", "K2", "K3", "K4", "K5", "K6"]
if counted_characters > 0:
    while len(K_list) > 1:
        split_index = (counted_characters % len(K_list) - 1)
        if split_index >= 0:
            right = K_list[split_index + 1:]
            left = K_list[:split_index]
            K_list = right + left
        else:
            K_list = K_list[:len(K_list)-1]
else:
    print("It seems that there are no common letters between both, please use different names or include another.")
#STEP 6
if K_list[0] == "K1":
    print("Relationship status: Kaibigan")
elif K_list[0] == "K2":
    print("Relationship status: Kapuso")
elif K_list[0] == "K3":
    print("Relationship status: Kaaway")
elif K_list[0] == "K4":
    print("Relationship status: Kasal")
elif K_list[0] == "K5":
    print("Relationship status: Kilig (crush)")
elif K_list[0] == "K6":
    print("Relationship status: Kapatid")