import random

def base_conversion():
    maximum_value = 10 ** 4 - 1
    print("The maximum number of base 10 value is " + str(maximum_value))

    base = int(input("Please enter a decimal number from 1 to 10: "))
    original_value = int(input("Please enter a number less than and equal: "))
    user_value = base ** 4 - 1

    print("The maximum value of the base is " + str(user_value))

    if original_value <= maximum_value:

        reminder1 = original_value % base
        quotient1 = original_value / base - reminder1 / base

        reminder2 = quotient1 % base
        quotient2 = quotient1 / base - reminder2 / base

        reminder3 = quotient2 % base
        quotient3 = quotient2 / base - reminder3 / base

        reminder4 = quotient3 % base

        final_result = str(int(reminder4)) + str(int(reminder3)) + str(int(reminder2)) + str(int(reminder1))

        print("The final result of your value is " + str(final_result) + ".")

    else:

        print("Your maximum value of the base " + str(base) + " is " + str(maximum_value) +
              ". Please enter another value.")

def roll_dice(number_of_roll, number_of_side):
    if number_of_roll >= 1:
        random_total = int(number_of_side) * int(number_of_roll)
        return random_total

def create_name(name_length):
    name = "abcdefghijklmnopqrstuvwxyz"
    name1 = name.upper()
    name2 = name.lower()
    alphabet_string = str(name1) + str(name2)
    if name_length < 0:
        return None
    else:
        random_alpha = random.choice(alphabet_string)
        generated_name = set()
        generated_name.append(random_alpha)
        if len(generated_name) == name_length:
            return random_alpha

if __name__ == '__main__':
    number_of_rolls = int(input("Please enter how many times you want to roll this round: "))
    number_of_sides = int(input("Please enter the number you rolled this round: "))
    roll_dice(number_of_rolls, number_of_sides)
    name_length_input = int(input("Please enter the length of your name wanted: "))
    create_name(name_length_input)
    base_conversion()