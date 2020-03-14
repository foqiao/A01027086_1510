

def most_vowels(tuple):
    vowel = ['a', 'e', 'i', 'o', 'u']
    tuple.count(vowel)


tuple_input = tuple(input("Please enter a combination of strings: "))
most_vowels(tuple_input)