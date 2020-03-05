def cube_root(pos_int):
    value_dictionary = []
    for value in range(0, pos_int):
        if value ** 3 < pos_int:
            pass
        elif value ** 3 == pos_int:

        else:
            print("No cube root for %d" % pos_int)

pos_int_input = int(input("Please enter a positive integer: "))
cube_root(pos_int_input)