def base_conversion():

    base = int(input("Please enter a base from 2 to 9: "))
    original_value = int(input("Please enter a number less than and equal: "))
    maximum_value = base ** 4 - 1

    print("The maximum value of the base is " + str(maximum_value))

    if original_value <= maximum_value:

        reminder1 = original_value % base
        quotient1 = original_value / base - reminder1 / base

        reminder2 = quotient1 % base
        quotient2 = quotient1 / base - reminder2 / base

        reminder3 = quotient2 % base
        quotient3 = quotient2 / base - reminder3 / base

        reminder4 = quotient3 % base

        final_result = str(int(reminder4)) + str(int(reminder3)) + str(int(reminder2)) + str(int(reminder1))

        print("The final result of your value is " + str(final_result) + ".")

    else:

        print("Your maximum value of the base " + str(base) + " is " + str(maximum_value) +
              ". Please enter another value.")


base_conversion()