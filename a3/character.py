"""Functions for creating a player character in a simple SUD."""

import random


# generate_x functions taken from Kyle's A2
def generate_vowel() -> str:
    """
    Return a string containing a random vowel.

    :precondition: No parameter is entered.
    :postcondition: Randomly selects and returns a vowel from the Latin alphabet.
    :return: Returns a string containing a single random vowel.
    """
    vowels = 'aeiouy'
    i = random.randint(0, len(vowels) - 1)
    return vowels[i]


def generate_consonant() -> str:
    """
    Return a string containing a random consonant.

    :precondition: No parameter is entered.
    :postcondition: Randomly selects and returns a consonant from the Latin alphabet.
    :return: Returns a string containing a single random consonant."""
    consonants = 'bcdfghjklmnpqrstvwxyz'
    i = random.randint(0, len(consonants) - 1)
    return consonants[i]


def generate_syllable() -> str:
    """
    Return a string containing a single consonant and a single vowel.

    :precondition: No argument is passed.
    :postcondition: Function returns a two-character string of a randomly generated consonant and vowel.
    :return: Returns a string containing a random consonant and a random vowel."""
    return generate_consonant() + generate_vowel()


# print(generate_syllable())
def generate_name(syllables: int) -> str:
    """
    Generate a random name with a given number of syllables.

    This function accepts one positive non-zero integer and returns a string of random syllables equal to that integer.
    Each syllable contains one consonant and one vowel.
    :param syllables: a positive non-zero integer
    :precondition: Integer is greater than zero.
    :postcondition: Function returns a string of given number of syllables, where each syllable is a random consonant
    followed by a random vowel.
    :return: Returns a randomly generated name.
    """
    name = ''
    n = 0
    while n < syllables:
        name = name + generate_syllable()
        n = n + 1
    return name.title()


def prompt_name() -> str:
    """
    Prompt the user to enter a name, or randomly generate a name.

    :precondition: No argument is passed to the function.
    :postcondition: User is prompted to enter a character name, or randomly generate a name of 1-6 syllables.
    :return: Returns a string of the user's input, or a randomly-generated string of alternating consonants and vowels.
    """
    valid_name = False
    while not valid_name:
        character_name = input("Please enter your character's name, or enter \"random\" for a random name: ")
        character_name = character_name.strip().lower()
        alphabet = [chr(i) for i in range(97, 123)]
        if set(character_name).issubset(set(alphabet)):
            valid_name = True
        else:
            print("PLease enter alphabetic characters only with no spaces in-between.")
    if character_name == 'random':
        syllables = random.randint(1, 6)
        character_name = generate_name(syllables)
    return character_name.title()


def create_character() -> dict:
    """
    Prompt a user to create a character for a simple SUD game.

    :precondition: No parameter is passed.
    :postcondition: Function generates a character with 10 max HP, starting at position [0, 0], with either a
    user-generated name or a randomly-generated name.
    :return: Returns a dictionary of the new character.
    """
    character = dict()
    character['Name'] = prompt_name()
    character['HP'] = [10, 10]
    character['Position'] = [0, 0]
    print(f"Character {character['Name']} created!")  # optional
    return character


def main():
    """Drive the program."""
    create_character()


if __name__ == '__main__':
    main()
