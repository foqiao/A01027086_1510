"""Functions associated with monster encounters. Run to test."""

import sud
import random
import doctest


def monster_randomizer() -> dict:
    monster_names = ['Crazed Brigand', 'Frostbite Spider', 'Beholder', 'Mangled Death Knight', 'Treeant', 'Unicorn',
                     'Dire Wolf', 'Shia Labeouf', 'Violent Bounty Hunter', 'Green Snail']
    i = random.randint(0, len(monster_names) - 1)
    return {'Name': monster_names[i], 'HP': [5, 5]}


# copied from Kyle's a2
def combat_initiative(opponent_one: dict, opponent_two: dict) -> list:
    initiative_one = sud.roll_die(1, 20)
    initiative_two = sud.roll_die(1, 20)
    while initiative_one == initiative_two:
        initiative_one = sud.roll_die(1, 20)
        initiative_two = sud.roll_die(1, 20)
    if initiative_one > initiative_two:
        print("%s attacks first." % (opponent_one['Name']))
        first_attacker = opponent_one
        second_attacker = opponent_two
    else:
        print("%s attacks first." % (opponent_two['Name']))
        first_attacker = opponent_two
        second_attacker = opponent_one
    return [first_attacker, second_attacker]


# copied/modified
def damage_roll(victim: dict) -> int:
    damage = sud.roll_die(1, 6)
    victim['HP'][1] -= damage
    return damage


# copied/modified
def attack(attacker: dict, victim: dict):
    attack_hits = (sud.roll_die(1, 4) > 1)
    if attack_hits:
        attack_damage1 = damage_roll(victim)
        print("%s strikes %s for %d damage!" % (attacker['Name'], victim['Name'], attack_damage1))
        print("%s has %d HP remaining." % (victim['Name'], victim['HP'][1]))
    else:
        print("%s\'s attack misses!" % (attacker['Name']))


# copied
def combat_round(opponent_one: dict, opponent_two:dict):
    initiative = combat_initiative(opponent_one, opponent_two)
    first_attacker = initiative[0]
    second_attacker = initiative[1]
    attack(first_attacker, second_attacker)
    if second_attacker['HP'][1] > 0:
        attack(second_attacker, first_attacker)
        if first_attacker['HP'][1] <= 0:
            print("%s has died!" % (first_attacker['Name']))
    else:
        print("%s has died!" % (second_attacker['Name']))


def encounter_dialogue(player: dict, monster: dict) -> str:
    print("%s has encountered a %s!" % (player['Name'], monster['Name']))
    player_choice = input("Will you RUN or FIGHT ? (Please enter your choice:) ")
    player_choice = player_choice.strip().lower()
    while player_choice != 'run' and player_choice != 'fight':
        print("Please enter either \'run\' or \'fight\'.")
        player_choice = input("Will you RUN or FIGHT ? ")
        player_choice = player_choice.strip().lower()
    return player_choice


def run_away(player: dict, monster: dict):
    monster_backstab = sud.roll_die(1, 10)
    if monster_backstab == 1:
        print("The %s manages to hit %s as they run away." % (monster['Name'], player['Name']))
        backstab_damage = sud.roll_die(1, 4)
        player['HP'][1] -= backstab_damage
        print("%s loses %d HP!" % (player['Name'], backstab_damage))
    else:
        print("%s successfully flees from battle unharmed!" % (player['Name']))


# consider randomizing text that is printed between user inputs
def monster_encounter(player: dict, monster: dict):
    player_choice = encounter_dialogue(player, monster)
    if player_choice == 'run':
        run_away(player, monster)
    elif player_choice == 'fight':
        print("%s braces for a fight to the death." % (player['Name']))
        round_num = 1
        while player['HP'][1] > 0 and monster['HP'][1] > 0:
            print("\n-- Round %d --\n" % round_num)
            combat_round(player, monster)
            round_num += 1
        if monster['HP'][1] <= 0:
            print("%s survives the battle with %d HP remaining." % (player['Name'], player['HP'][1]))
        if player['HP'][1] <= 0:
            # consider implementing a game-over function and placing it here
            print('%s has fallen!' % player['Name'])


def healing(player: dict):
    """elements and blocks needed for healing process"""
    player_hp = player['HP'][1]
    hp_needs = 10 - player_hp
    """if-else added to testify the need of healing for the player"""
    if player_hp < 10:
        player['HP'][1] = player_hp + hp_needs
        print('%s healed for %d HP. (now at %d/%d)' % (player['Name'], hp_needs, player['HP'][1], player['HP'][0]))
    else:
        print('The player has no need to heal.')


def main():
    """Drive the program."""
    bob = {'Name': 'Bob', 'HP': [10, 10]}
    monster1 = monster_randomizer()
    monster_encounter(bob, monster1)
    print(bob, monster1)
    healing(bob)
    doctest.testmod()


if __name__ == '__main__':
    main()
