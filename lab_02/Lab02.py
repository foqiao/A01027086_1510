import random

def roll_dice(number_of_roll, number_of_side):
    if number_of_roll >= 1:
         random_total = int(number_of_side) * int(number_of_roll)
         print("Your value is " + str(random_total))
    else:
         print("It is impossible to calculate the result.")

def create_name(name):
    name = input_name.title()
    if int(len(name)) > 0:
        print("Your name is " + name)
    else:
        return None
if __name__ == '__main__':
    number_of_rolls = int(input("Please enter how many times you want to roll this round: "))
    number_of_sides = int(input("Please enter the number you rolled this round: "))
    roll_dice(number_of_rolls, number_of_sides)
    input_name = str(input("Please enter a name you want to have: "))
    create_name(input_name)