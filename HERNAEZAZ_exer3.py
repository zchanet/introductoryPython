# Application of learnings about modular programming by the designing and writing of own functions in Python:

x = ''
y = ''

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_odd(y):
    if y % 2 != 0:
        return True
    else:
        return False

def ask_inputs(x, y):
    while True:
        x = int(input("\nEnter value for x: "))
        y = int(input("Enter value for y: "))
        if x < 0 or y < 0:
            print("x and y must be both POSITIVE integers!")
        elif x % 2 != 0:
            print("x must be an EVEN integer!")
        elif y % 2 == 0:
            print("y must be an ODD integer!")
        elif is_even(x) and is_odd(y):
            return x, y
x, y = ask_inputs(x, y)
# print(x)
# print(y)

def calculate_total_squares(x):
    for i in range(1, x+1):
        if is_even(i):
            i = i ** 2
            i += i ** 2
            return i

def create_pattern(y):
    for i in range(y):
        for j in range(y):
            print("* ", end="")
        print()

def calculate_average(x):
    for i in range(1, x+1):
        if is_odd(i):
            i += i
    average = 0
    average = i / (len(range(1, x+1))//2)
    return average

choice = ''

def check_choice(choice):
    print("\nPlease choose from the following: \n\t[1] Summation\n\t[2] Box\n\t[3] Average\n\t[0] Exit")
    choice = (input("Enter your choice: "))
    check_choice.choice = choice
    if choice != "0":
        return True
    else:
        return False

while check_choice(choice):
    c = check_choice.choice
    if c == "1":
        print(f"\nThe sum of the squares of all even integers from 1 to {x} is {calculate_total_squares(x)}")
    elif c == "2":
        create_pattern(y)
    elif c == "3":
        print(f"\nThe average of odd integers from 1 to {x} is {calculate_average(x)}")
    elif c == "O":
        print('\nYou probably made a mistake as the number "0" and capital letter "O" look similar at first glance.\nIf you wish to exit the program, enter the number zero.')
    else:
        print("\nYour input isn't among the choices. Please try again.")
print("\nGoodbye! Have a great day!")