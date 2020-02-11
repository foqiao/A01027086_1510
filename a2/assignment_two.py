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
                                "Monk": 6, "Bard": 7, "Druid": 8, "Paladin": 9, "Sorcerer": 10, "Warlock": 11,
                                0: range(100, 0, -1), 1: range(100, 0, -1), 2: range(100, 0, -1), 3: range(100, 0, -1),
                                4: range(100, 0, -1), 5: range(100, 0, -1), 6: range(100, 0, 1), 7: range(100, 0, 1),
                                8: range(100, 0, 1), 9: range(100, 0, 1), 10: range(100, 0, 1), 11: range(100, 0, 1)}
            player_second_response_storage = player_second_response
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

    shop_items = ["sword", "dagger", "chalice of becoming", "orb of discovery"]
    bag_list = []

    print("Here is the list of outfits you can have, ")
    print("1.sword")
    print("2.dagger")
    print("3.chalice of becoming")
    print("4.orb of discovery")
    print("5.more")
    print("-1.finish")

    if outfit == 1:
        print("sword is what you want")
        bag_list.append("sword")
        if random.choice(bag_list) == random.choice(shop_items):
            print("You already have sword")
    elif outfit == 2:
        print("dagger is what you want")
        bag_list.append("dagger")
        if random.choice(bag_list) == random.choice(shop_items):
            print("You already have dagger")
    elif outfit == 3:
        print("chalice of becoming is what you want")
        bag_list.append("chalice of becoming")
        if random.choice(bag_list) == random.choice(shop_items):
            print("You already have chalice of becoming")
    elif outfit == 4:
        print("orb of discovery is what you want")
        bag_list.append("orb of discovery")
        if random.choice(bag_list) == random.choice(shop_items):
            print("You already have orb of discovery")
    elif outfit == 5:
        print("nothing is available yet")

    choice = int(input("Do you want to leave? (-1 for exit):"))
    if choice == -1:
        exit(outfit)

def combat_round(opponent1, opponent2, roles_of_classes, inventory, Monsters):
    Player_choice = str(input("Please enter the inventory you want to fight the monster(e.g. Sword, Shield, Knife): "))

    opponent1 = player_second_response_storage
    opponent2 = Monsters
    Individual_fighter = random.choice(opponent1)
    Individual_monster = random.choice(opponent2)

    if Player_choice == inventory[0]:
        Individual_monster_blood = range(100, 0, -1)
        Individual_monster_lose = Individual_monster_blood - 1

    exp = 0

    if Individual_monster == 0:
        exp_incline = int(exp) + 1
        opponent2.remove(Individual_monster)
        print("Hooray!")
        print(opponent2)
        print(exp_incline)

    elif Player_choice == inventory.index(1, 2):
        Individual_monster_remain = range(100, 0, -1)
        Individual_monster_lose = Individual_monster_remain
        print("Dodge!")
        print(opponent2)

    elif Player_choice != random.choice(inventory):
        roles = random.choice(roles_of_classes)

        roles_blood = roles - 1

    else:
        print("Warning! Invalid input")
        roles = random.choice(roles_of_classes)
        roles_blood = roles - 1

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

    opponent1_1 = player_second_response_storage
    Monsters1 = ["M1", "M2", "M3"]
    opponent2_1 = Monsters1

    roles_of_classes1 = {"fighter": 0, "barbarian": 1, "cleric": 2, "ranger": 3, "rogue": 4, "wizard": 5,
                            "Monk": 6, "Bard": 7, "Druid": 8, "Paladin": 9, "Sorcerer": 10, "Warlock": 11,
                            0: range(100, 0, -1), 1: range(100, 0, -1), 2: range(100, 0, -1), 3: range(100, 0, -1),
                            4: range(100, 0, -1), 5: range(100, 0, -1), 6: range(100, 0, 1), 7: range(100, 0, 1),
                            8: range(100, 0, 1), 9: range(100, 0, 1), 10: range(100, 0, 1), 11: range(100, 0, 1)}

    old_user_inventory = {
        "Sword": 1,
    }
    new_user_inventory = {
        "Knife": 1
    }

    inventory1 = old_user_inventory or new_user_inventory

    combat_round(opponent1_1, opponent2_1, roles_of_classes1, inventory1, Monsters1)