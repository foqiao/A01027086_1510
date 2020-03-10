import random


def roll_die(num_of_rolls, num_of_sides):
    rolled_sum = range(num_of_sides, num_of_rolls * num_of_sides - 1)
    for i in rolled_sum:
        print(i)

num_of_rolls1 = int(input("Please enter how many times you want to roll a die: "))
num_of_sides1 = int(input("Please enter how many sides you want your die to be: "))
roll_die(num_of_rolls1, num_of_sides1)

def create_name(length):
    name_string = []
    letter = "abcdefghijklmnopqrstuvwxyz"

    letter_picker = random.choice(letter)
    name_string.append(letter_picker)

    if len(name_string) == length:
        print(name_string)

length1 = 