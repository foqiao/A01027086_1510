def most_vowels(tuple):
    vowels_in_string = {}
    tuple_range = range(0, len(tuple) + 1)
    mul_vowels = range(1, len(tuple) + 1)
    for i in tuple_range:
        for j in mul_vowels:
            if tuple[i] == 'a' * j:
                vowels_in_string.update({i: tuple[i]})
            elif tuple[i] == 'e' * j:
                vowels_in_string.update({i: tuple[i]})
            elif tuple[i] == 'i' * j:
                vowels_in_string.update({i: tuple[i]})
            elif tuple[i] == 'o' * j:
                vowels_in_string.update({i: tuple[i]})
            elif tuple[i] == 'u' * j:
                vowels_in_string.update({i: tuple[i]})

tuple_input = tuple(input("Please enter a combination of strings: "))
most_vowels(tuple_input)