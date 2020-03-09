def base_conversion():
    num = int(input("Please enter a base 10 number: "))
    new_base = int(input("Please enter the new base you want the base 10 number convert to: "))

    max_num_of_new_base = new_base ** 4 - 1
    print("The maximum number of the new base is " + str(max_num_of_new_base))

    for i in range(num, -1, new_base):
        converted_value = []
        quotient = i // new_base
        reminder = i % new_base
        converted_value.append(reminder)
        print(converted_value)

base_conversion()