import random

def roll_dice():
    number_of_rolls = random.randint(1, 100)
    number_of_side = random.randint(1, 6)

    if number_of_rolls >= 1:
         random_total = int(number_of_side) * int(number_of_rolls)
         print("Your value is " + str(random_total))
    else:
         print("It is impossible to calculate the result.")

roll_dice()

def create_name(name):
    name = input_name.title()
    if int(len(name)) > 0:
        print("Your name is " + name)
    else:
        return None

input_name = str(input("Please enter a name you want to have: "))
create_name(input_name)