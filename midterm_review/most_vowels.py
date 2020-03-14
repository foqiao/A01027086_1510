import random


def most_vowels(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    vowel_in_string = []
    vowel_ranking = []
    for i in range(0, len(string) - 1):
        for j in range(0, len(string[i]) - 1):
            if string[i][j] == random.choice(vowel):
                vowel_in_string.append(string[i][j])
                vowel_ranking.append(len(vowel_in_string))
            else:
                pass
        vowel_ranking.sort(reverse=True)
        print(vowel_ranking)

string_input = str(input("Please enter a combination of strings: "))
most_vowels(string_input)