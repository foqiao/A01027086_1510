"""Play a simple text-based Single User Dungeon."""

import random


# taken from Kyle's a2 package
def roll_die(number_of_rolls, number_of_sides):
    """
    Simulate rolling a die with a given number of sides x times and return the sum of the rolls.

    :param number_of_rolls: a positive integer
    :param number_of_sides: a positive non-zero integer
    :precondition: Both integers are positive.
    :postcondition: Function returns a sum of simulated dice rolls.
    :return: Returns the sum of the dice rolls.
    """
    completed_rolls = 0
    roll_sum = 0
    while completed_rolls < number_of_rolls:
        roll_sum = roll_sum + random.randint(1, number_of_sides)
        completed_rolls = completed_rolls + 1
    return roll_sum


def main():
    """Drive the program."""


if __name__ == '__main__':
    main()
