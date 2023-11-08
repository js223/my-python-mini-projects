import random
def dice_number_1():
    print("===========")
    print("|         |")
    print("|    0    |")
    print("|         |")
    print("===========")

def dice_number_2():
    print("===========")
    print("|         |")
    print("|0       0|")
    print("|         |")
    print("===========")

def dice_number_3():
    print("===========")
    print("|    0    |")
    print("|    0    |")
    print("|    0    |")
    print("===========")

def dice_number_4():
    print("===========")
    print("|0       0|")
    print("|         |")
    print("|0       0|")
    print("===========")

def dice_number_5():
    print("===========")
    print("|0       0|")
    print("|    0    |")
    print("|0       0|")
    print("===========")

def dice_number_6():
    print("===========")
    print("|0       0|")
    print("|0       0|")
    print("|0       0|")
    print("===========")


dice_decision = 'y'

while dice_decision == 'y':
    print("This is a dice simulator")
    random_integer = random.randint(1,6)
    if random_integer == 1:
        dice_number_1()
    elif random_integer == 2:
        dice_number_2()
    elif random_integer == 3:
        dice_number_3()
    elif random_integer == 4:
        dice_number_4()
    elif random_integer == 5:
        dice_number_5()
    elif random_integer == 6:
        dice_number_6()
    print("Press y to roll again")
    dice_decision = input()