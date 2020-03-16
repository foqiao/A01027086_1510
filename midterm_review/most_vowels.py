def most_vowels(tuple):
    vowel_in_tuple = []
    vowel_in_string = []
    tuple_of_string = range(0, len(tuple))
    for i in tuple_of_string:
        if tuple[i] == ',':
           vowel_in_tuple.append(" ")
        if tuple[i] == 'a':
            vowel_in_tuple.append(tuple[i])
        if tuple[i] == 'e':
           vowel_in_tuple.append(tuple[i])
        if tuple[i] == 'i':
            vowel_in_tuple.append(tuple[i])
        if tuple[i] == 'o':
            vowel_in_tuple.append(tuple[i])
        if tuple[i] == 'u':
            vowel_in_tuple.append(tuple[i])
    print(vowel_in_tuple)

tuple_input = tuple(input("Please enter a combination of strings(must separated by comma): "))
most_vowels(tuple_input)