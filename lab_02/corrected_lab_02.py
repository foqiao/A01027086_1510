import random
import string

def roll_die(num_of_rolls, num_of_sides):
    rolled_sum = range(num_of_sides, num_of_rolls * num_of_sides - 1)
    for i in rolled_sum:
        print(i)

num_of_rolls1 = int(input("Please enter how many times you want to roll a die: "))
num_of_sides1 = int(input("Please enter how many sides you want your die to be: "))
roll_die(num_of_rolls1, num_of_sides1)

def create_name(length):
    alpha = string.ascii_lowercase
    letter_picker = random.choice(alpha)
    print(letter_picker)

length1 = int(input("Please enter the length of the name you want to have: "))
create_name(length1)