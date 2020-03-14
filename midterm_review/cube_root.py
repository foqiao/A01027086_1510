def cube_root(pos_int):
    for i in range(0, pos_int):
        if i ** 3 < pos_int:
            pass
        if i ** 3 == pos_int:
            print(i)
            print("We found the root")
            break
        if i ** 3 > pos_int:
            print("No roots for this pos_int")
            break

pos_int_input = int(input("Please enter a positive integer: "))
cube_root(pos_int_input)