def roman_numeral(pos_int):
    roman_string = []
    digit = [1000, 500, 100, 50, 10, 5, 1]
    digit.sort(reverse=True)
    for i in (0, len(pos_int)):
        if i < 4:
            amount = i * "I"
            roman_string.append(amount)
        if 10 > i > 6:
            amount