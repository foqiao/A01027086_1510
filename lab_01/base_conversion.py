def base_conversion():
    num = int(input("Please enter a base 10 number: "))
    new_base = int(input("Please enter the new base you want the base 10 number convert to: "))

    if 2 <= new_base <= 9:
        max_num_of_new_base = new_base ** 4 - 1
        print("The maximum number of the new base is " + str(max_num_of_new_base))

        quotient = num // new_base
        reminder = num % new_base

        quotient1 = quotient // new_base
        reminder1 = quotient % new_base

        quotient2 = quotient1 // new_base
        reminder2 = quotient1 % new_base

        quotient3 = quotient2 // new_base
        reminder3 = quotient2 % new_base

        converted_value = int(str(reminder3) + str(reminder2) + str(reminder1) + str(reminder))
        print(int(converted_value))
    else:
        print("Out of range")

if __name__ == '__main__':
    base_conversion()