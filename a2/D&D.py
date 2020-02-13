import random
import string
from numpy import NaN


def roll_dice(number_of_roll, number_of_side):
    number_of_roll = random.randint(1, 3)
    number_of_side = random.randint(1, 12)

    sum_roll_dice = number_of_roll * number_of_side
    return sum_roll_dice

def generate_name(syllable):
    vowel = "aeiouy"
    alphabet_string = string.ascii_lowercase
    consonent = alphabet_string.remove(vowel)

    syllable = random.choice(vowel) + random.choice(consonent)
    return syllable

def create_character(character_syllable):
    if character_syllable < 0:
        print("Warning")
        return None
    elif 1 <= character_syllable <= 10:
        character_dictionary = {
            1: 'Elf',
            2: 'Orc',
            3: 'Warrior',
            4: 'Barbarian',
            5: 'Wizard',
            6: 'Alagon',
            7: 'Sorrow'
            8: 'Mayday',
            9: 'Katniss Everdeen'
            10: 'Wu'
        }
    else:
        print("not yet")
        return None

def choose_inventory(outfit):

    outfit = {
        "sword": 1,
        "dagger": 2,
        "chalice of becoming": 3,
        "orb of discovery": 4,
        "Herb": 5,
        "Malaysian Sword": 6,
        "Upgrade defense": 7,
        "more": 8,
        "Special Curse": 9,
        "-1": exit(outfit)
    }

    return outfit

    purchased_items = {
        "knife": 1,
        "shield": 2
    }

    if shop_items.values() >= 10 || shop_items.values() <= 0:
        purchased_items = random.randrange(outfit.values(3), outfit.values(9));


def combat_round(Player_spec, number_of_sides, number_of_rolls):
    picked_character = {
        "health": range(100, 0, -1),
        "weapon": bag_list
    }
    picked_second_character = {
        "health": range(100, 0, -1),
        "weapon": bag_list
    }
    return picked_character
    Monster_specs = {
        "health": range(100, 0, -1),
        "weapon": None
    }
    for number_of_sides in range(1, 12):
        if number_of_rolls

if __name__ == '__main__':
    player_response = int(input("Please enter the side of your first roll(e.g. 1, 2): "))
    player_second_response = int(input("Please enter the side of your second roll(e.g. 1, 2): "))
    player_third_response = int(input("Please enter the side of your third roll(e.g. 1, 2): "))

    final_syllable_output_index = str(player_response) + str(player_second_response) + str(player_third_response)

    number_of_roll = range(1, 3, 1)
    number_of_side = range(1, 12, 1)

    roll_dice(number_of_roll, number_of_side, final_syllable_output_index)

    syllable = final_syllable_output_index

    generate_name(syllable)

    create_character(syllable)

    character1 = final_syllable_output_index

    print_character(character1, player_response, player_second_response, player_third_response)

    outfit1 = str(input("Please enter the outfit you want to have by initial number(e.g. 1 for 1.Sword): "))

    choose_inventory(outfit1)

    Player_roll = int(input("Please enter the number of rolls you want to have:"))
    Monster_roll = random.choice(number_of_roll)

    bag_list = int(input("Please enter the index value of the weapon you want from 0-first_weapon to ##-last " +
                              "weapon: "))

    Player_specs1 = {
        "health": range(100, 0, -1),
        "weapon": bag_list
    }
    del Player_specs1["weapon"]

    current_bag_list1 = {
        "knife": 1,
        "shield": 2
    }

    if int(bag_list) == range(current_bag_list1.index(0), current_bag_list1.index(-1)):
        Player_specs1["weapon"] = current_bag_list1.index(int(bag_list))
    else:
        print("Invalid index value")

    combat_round(Player_specs1, Player_roll, Monster_roll)