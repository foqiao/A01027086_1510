import random
import string
from numpy import NaN


def roll_dice(number_of_roll, number_of_side):
    if number_of_side <= 12 or number_of_side < 0:
        if number_of_roll and number_of_side != NaN:
            sum_roll_dice = int(number_of_roll) * int(number_of_side)
            print(sum_roll_dice)
        else:
            return None

def generate_name(syllable):
    vowel = "aeiouy"
    alphabet_string = string.ascii_lowercase
    consonent = alphabet_string.remove(vowel)

    syllable = random.choice(vowel) + random.choice(consonent)
    return syllable

def create_character(character_syllable, second_character_syllables):
    if int(character_syllable) < 0 or int(second_character_syllables) < 0:
        print("Warning")
        return None
    elif 1 <= int(character_syllable) <= 10 or 1 <= int(second_character_syllables) <= 10:
        character_dictionary = {
            1: 'Elf',
            2: 'Orc',
            3: 'Warrior',
            4: 'Barbarian',
            5: 'Wizard',
            6: 'Alagon',
            7: 'Sorrow',
            8: 'Mayday',
            9: 'Katniss Everdeen',
            10: 'Wu'
        }
        character_syllable = random.choice(character_dictionary)
        second_character_syllables = random.choice(second_character_syllables)
        return character_syllable
        return second_character_syllables
    else:
        print("not yet")
        return None

def choose_inventory():

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
        "-1": "exit"
    }

    return outfit

    outfits = int(input("Please enter the index number of items you want to buy: "))

    purchased_item = {
        "knife": 1,
        "shield": 2
    }

    if int(outfits) >= 10 & int(outfits) <= 0:
        purchased_item = random.randrange(outfit.values(3), outfit.values(9))
    if int(outfits) == -1:
        exit()

def combat_round():
    picked_character = character_syllables
    picked_second_character = second_character_syllable
    picked_character = {
        "health": range(100, 0, -1),
        "weapon": purchased_items
    }
    picked_second_character = {
        "health": range(100, 0, -1),
        "weapon": purchased_items
    }

    return picked_character
    return picked_second_character

    monster = {
        "health": range(100, 0, -1),
        "weapon": None
    }

    return monster

    for number_of_side in range(1, 12):
        player_roll = random.choice(number_of_sides)
        monster_roll = random.choice(number_of_sides)
        if player_roll == monster_roll:
            player_roll = random.choice(number_of_sides)
            monster_roll = random.choice(number_of_sides)
        elif player_roll < monster_roll:
            player_roll["health"] -= 1
        elif player_roll > monster_roll:
            monster_roll["health"] -= 1
        else:
            return None

def purchased_items():
    pass

if __name__ == '__main__':
    number_of_rolls = int(input("Please enter how times you want to roll: "))
    number_of_sides = int(input("Please enter the side you want to pick for each roll: "))
    roll_dice(number_of_rolls, number_of_sides)

    character_syllables = int(input("Please enter a number between 1 and 10 randomly: "))
    second_character_syllable = int(input("Please enter a number between 1 and 10 randomly: "))
    create_character(character_syllables, second_character_syllable)

    choose_inventory()

    combat_round()