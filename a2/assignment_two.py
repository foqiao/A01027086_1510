import random

from numpy import NaN


def roll_dice(number_of_rolls, number_of_sides, syllable_output_index):
    if player_response == random.choice(number_of_roll):
        syllable_output_index[0] = player_response
    elif player_second_response == random.choice(number_of_roll):
        syllable_output_index[1] = player_second_response
    elif player_third_response == random.choice(number_of_roll):
        syllable_output_index[2] = player_third_response
    else:
        return None

    number_of_rolls = range(1, 3, 1)
    number_of_sides = range(1, 12, 1)

def generate_name(syllable0):
    syllable0 = syllable_output_index
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']

    def generate_vowel():
        if syllable[0] == vowel.index(0, 5):
            vowel_output = syllable[0]
            syllable[0] = str(vowel_output)
        else:
            return None

    def generate_consonant():
        if syllable[1] != vowel.index(0, 5):
            consonant_output = syllable[1] or 'y'
            syllable[-1] = str(consonant_output)
        else:
            return None

    return syllable

def create_character(syllable1, syllable_output_index):
    syllable_output_index2 = syllable_output_index
    player = []
    player_name = generate_name(syllable1)
    player.append(player_name)

    def select_class(dice_of_classes, roles_of_classes, races_of_classes):
        if player_response == random.choice(str(dice_of_classes)):
            dice_of_classes = {
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "10": 10,
                "11": 11,
                "12": 12
            }
            player_response_storage = player_response
        else:
            print("Warning! Invalid input!")

        player_second_response1 = int(input("Please enter the side of your second roll(e.g. 1, 2): "))
        if player_second_response1 == random.choice(roles_of_classes):
            roles_of_classes = {"fighter": 0, "barbarian": 1, "cleric": 2, "ranger": 3, "rogue": 4, "wizard": 5,
                                "Monk": 6, "Bard": 7, "Druid": 8, "Paladin": 9, "Sorcerer": 10, "Warlock": 11 }
            roles_of_classes_health = {0: range(100, 0, -1), 1: range(100, 0, -1), 2: range(100, 0, -1), 3: range(100, 0, -1),
                                4: range(100, 0, -1), 5: range(100, 0, -1), 6: range(100, 0, 1), 7: range(100, 0, 1),
                                8: range(100, 0, 1), 9: range(100, 0, 1), 10: range(100, 0, 1), 11: range(100, 0, 1)}
            player_second_response_storage = roles_of_classes
        else:
            print("Warning! Invalid input!")

        player_third_response1 = int(input("Please enter the side of your third roll(e.g. 1, 2): "))
        if player_third_response1 == random.choice(races_of_classes.index()):
            races_of_classes = {
                "human": 1,
                "warrior": 2,
                "drawf": 3,
                "ranger": 4,
                "rogue": 5,
                "wizard": 6,
                "witch": 7,
                "half-elf": 8,
                "half-elf1": 9,
                "half-orc": 10,
                "god": 11,
                "half-elf2": 12
            }
            player_third_response_storage = player_third_response
        else:
            print("Warning! Invalid input!")

    if random.choice(syllable) == NaN:
        print("Warning! This input is invalid!")
        return None
    elif random.choice(syllable) < 1:
        print("Warning! This input is invalid!")
        return None
    else:
        current_HP = random.choice(dice_of_classes)

        HP = {
            "max_HP": 20,
            "current_HP": current_HP
        }

        if current_HP > int("max_HP"):
            print("Sorry, out of range")
            return None

        if current_HP == random.choice(number_of_side):
            dictionary = {
                "Strength": 1,
                "Intelligence": 2,
                "Wisdom": 3,
                "Dexterity": 4,
                "Constitution": 5,
                "Charisma": 6
            }

        if syllable == random.choice(player):
            inventory = {
                "Sword": 1,
                "Shield": 2,
                "Armour": 3
            }
        else:
            inventory = {
                "Knife": 1
            }

    Monsters = ["M1", "M2", "M3"]
    return Monsters

    Monsters[0] = range(200, 0, -1)
    Monsters[1] = range(200, 0, -1)
    Monsters[2] = range(200, 0, -1)
    return Monsters

def print_character(character, player_response_storage, player_second_response_storage,
                    player_third_response_storage):
    character = str(player_response_storage) + str(player_second_response_storage) \
                + str(player_third_response_storage)

def choose_inventory(outfit):

    shop_items = {
        "sword": 1,
        "dagger": 2,
        "chalice of becoming": 3,
        "orb of discovery": 4,
        "Herb": 5,
        "Malaysian Sword": 6,
        "Upgrade defense": 7,
        "more": 8,
        "Special Curse": 9
    }

    return shop_items

    current_bag_list = {
        "knife": 1,
        "shield": 2
    }

    print(current_bag_list)

    if outfit == 1:
        print("sword is what you want")
        bag_list[-1].append("sword")
        if random.choice(bag_list) == "sword":
            print("You already have sword")
    elif outfit == 2:
        print("dagger is what you want")
        bag_list[-1].append("dagger")
        if random.choice(bag_list) == "dagger":
            print("You already have dagger")
    elif outfit == 3:
        print("chalice of becoming is what you want")
        bag_list[-1].append("chalice of becoming")
        if random.choice(bag_list) == "chalice of becoming":
            print("You already have chalice of becoming")
    elif outfit == 4:
        print("orb of discovery is what you want")
        bag_list[-1].append("orb of discovery")
        if random.choice(bag_list) == "orb of discovery":
            print("You already have orb of discovery")
    elif outfit == 5:
        print("Herb")
    elif outfit == 6:
        print("Malaysian Sword")
        bag_list[-1].append("Malaysian Sword")
        if random.choice(bag_list) == "Malaysian Sword":
            print("You already have Malaysian Sword")
    elif outfit == 7:
        print("upgrade defense is what you want")
        bag_list[-1].append("upgrade defense")
        if random.choice(bag_list) == "upgrade defense":
            print("You already have upgrade defense")
    elif outfit == 8:
        print("more coming")
    elif outfit == 9:
        print("Special Curse is what you want")
        bag_list[-1].append("Special Curse")
        if random.choice(bag_list) == "Special Curse":
            print("Another Special Curse is what you want")
    elif outfit != NaN:
        print("invalid, try again")
    else:
        exit(outfit)

def combat_round(Player_spec, Player_roll1, Monster_roll1):
    Player_specs = {
        "health": range(100, 0, -1),
        "weapon": bag_list
    }
    print(Player_specs)

    Monster_specs = {
        "health": range(100, 0, -1),
        "weapon": None
    }
    print(Monster_specs)

    Player_dice = random.choice(number_of_side)
    Player_attack = int(Player_roll) * int(Player_dice)

    Monster_dice = random.choice(number_of_side)
    Monster_attack = int(Monster_roll) * int(Monster_dice)

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