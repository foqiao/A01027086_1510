import random

from numpy.core import number


def convert_to_roman_numeral(positive_int):
    """
            convert arabic numeral to roman numeral

    :param positive_int: the input user want to convert to roman numeral
    :precondition: convert positive_int parameter to roman numeral resultant
    :post-condition: the function process specific algorithms for each unique roman numeral letters represent
    a different amount
    :return: return roman numerals represent the input value

    >>>convert_to_roman_numeral(1000)
    M
    >>>convert_to_roman_numeral(500)
    D
    >>>convert_to_roman_numeral(100)
    C
    >>>convert_to_roman_numeral(50)
    L
    >>>convert_to_roman_numeral(10)
    X
    >>>convert_to_roman_numeral(5)
    V
    >>>convert_to_roman_numeral(1)
    I
    """
    if 10000 >= positive_int >= 1:

        first_quotient = positive_int / 1000
        first_reminder = positive_int % 1000

        second_quotient = first_reminder / 500
        second_reminder = first_reminder % 500

        third_quotient = second_reminder / 100
        third_reminder = second_reminder % 100

        fourth_quotient = third_reminder / 50
        fourth_reminder = third_reminder % 50

        fifth_quotient = fourth_reminder / 10
        fifth_reminder = fourth_reminder % 10

        sixth_quotient = fifth_reminder / 5
        sixth_reminder = fifth_reminder % 5

    else:
        return None

    print(str(int(first_quotient) * "M") + str(int(second_quotient) * "D") + str(int(third_quotient) * "C") +
          str(int(fourth_quotient) * "L") + str(int(fifth_quotient) * "X") + str(int(sixth_quotient) * "V") +
          str(int(sixth_reminder) * "I"))


input_positive_int = int(input("Please enter a number (1 <= n <= 10000) you want to transfer to roman numeral: "))
convert_to_roman_numeral(input_positive_int)


def colour_mixer():
    """
            combinations of two colours picked by client to create a new colour

    :param: first_colour_input and second_colour_input
    :precondition: two colours suppose to merge into a new colour
    :post-condition: two colours matches the conditions enlisted will return stated values, otherwise, re-enter the
    colours
    :return: the colour result of combining two primary colours
    >>>'Please enter one of the three primary colours: blue'
    >>>'Please enter another one of the three primary colours: yellow'
    green
    """

    first_colour_input = str(input("Please enter one of the three primary colours (red, yellow, blue): "))
    second_colour_input = str(input("Please enter another one of the three primary colours (red, yellow, blue): "))
    if str(first_colour_input) != str(second_colour_input):
        if str(first_colour_input) == "red" and str(second_colour_input) == "blue":
            print("purple")
        elif str(first_colour_input) == "blue" and str(second_colour_input) == "red":
            print("purple")
        elif str(first_colour_input) == "red" and str(second_colour_input) == "yellow":
            print("orange")
        elif str(first_colour_input) == "yellow" and str(second_colour_input) == "red":
            print("orange")
        elif str(first_colour_input) == "blue" and str(second_colour_input) == "yellow":
            print("green")
        elif str(first_colour_input) == "yellow" and str(second_colour_input) == "blue":
            print("green")
        else:
            return None


colour_mixer()


def time_calculator(second):
    """
                    calculate seconds through different units consists by seconds
    :param second: contains seconds user's want to calculate into specific unit representation
    :precondition: seconds convert to a new value with a different unit measurement
    :post-condition: when seconds' value meets a specific range of the ranges listed, convert the seconds completely
    into the unit it represents
    :return: return the result after a series of filtration and execution
    >>>time_calculator(86400)
    1d
    """
    if int(int(second) / 86400) >= 1:
        print(str(int(second) / 86400) + str("d"))
    elif int(int(second) / 3600) >= 1:
        print(str(int(second) / 3600) + str("h"))
    elif int(int(second) / 60) >= 1:
        print(str(int(second) / 60) + str("min"))
    elif int(int(second)) < 60:
        print(str(int(second)) + str("sec"))
    else:
        return None


input_second = int(input("Please enter a time in second you currently think of: "))
time_calculator(input_second)


def compound_interest(principal, annual_interest_rate, annual_compound_time_of_interest_rate, time_duration):
    """
                        calculate the interested added value so far
    :param principal: initial deposit when the account created
    :param annual_interest_rate: interest rate each year since the plan is chosen by the client
    :param annual_compound_time_of_interest_rate: how many times a year the interest is added to the account
    :param time_duration: the time have spent for the account since the year it created
    :return: return the amount of principal remained in the account
    """
    Amount = float(principal) * float(1 + float(annual_interest_rate) / float(annual_compound_time_of_interest_rate)) \
             ** float(float(annual_compound_time_of_interest_rate) * float(annual_interest_rate))
    print(float(Amount))


input_principal = float(input("Please enter the initial value of your bank account: "))
input_annual_interest_rate = float(input("Please enter the annual interest rate of your plan: "))
input_annual_time_of_interest_rate = \
    float(input("Please enter how many times the your interest rate compounded annually: "))
input_time_duration = float(input("Please enter the years of the bank account since it created initially: "))
compound_interest(input_principal, input_annual_interest_rate, input_annual_time_of_interest_rate, input_time_duration)


def rock_paper_scissors():
    """
                a gaming application for clients to randomly roll gestures to see whether he/she beaten the opponents
                virtually appeared
    :param: Player: input value manually set by real-world clients
    :precondition: input value should clashes with the virtual opponent
    :post-condition: input value through a nest if-else clauses within another if-else clauses to figure-out what
    computer chooses randomly and who declare victory in each round
    :return: return the result of each round between a computer and a human player
    """
    comp = random.randint(1, 3)

    Player = str(input("Please enter rock, paper or scissors you want to beat the computer: "))

    if int(len(str(Player))) > 0 and str(Player) == "rock":
        if comp == 1:
            print("You lose")
            return comp
        elif comp == 2:
            print("You win")
            return comp
        elif comp == 3:
            print("Try again")
            return comp
        else:
            print("Please enter a gesture within the range(rock, paper, scissors)")
    elif int(len(str(Player))) > 0 and str(Player) == "paper":
        if comp == 1:
            print("You lose")
            return comp
        elif comp == 2:
            print("You lose")
            return comp
        elif comp == 3:
            print("You win")
            return comp
        else:
            print("Please enter a gesture within the range(rock, paper, scissors)")
    elif int(len(str(Player))) > 0 and str(Player) == "scissors":
        if comp == 1:
            print("You win")
            return comp
        elif comp == 2:
            print("You lose")
            return comp
        elif comp == 3:
            print("You lose")
            return comp
    else:
        return None


rock_paper_scissors()


def number_generator():
    """
                        generator six unique numbers in a roll as a lottery result
    :precondition: random_number should ranged in a string of numbers
    :post-condition: random_number will be generator through wildcard operations which led out a result which will be
    inspected by client manually from the result on console
    :return: the generated value from the function will output in console
    123456
    """
    random_number = random.randint(1, 49)
    first_num = int(random_number)
    second_num = int(random_number)
    third_num = int(random_number)
    fourth_num = int(random_number)
    fifth_num = int(random_number)
    sixth_num = int(random_number)
    if first_num != second_num != third_num != fourth_num != fifth_num != sixth_num:
        random_number_string = str(int(first_num)) + str(int(second_num)) + str(int(third_num))
        + str(int(fourth_num)) + str(int(fifth_num)) + str(int(sixth_num))
        random_number_string.sort(1, 49)

        print(str(random_number_string))
    else:
        return None

number_generator()


def number_translator():
    """
                        translate a 10 letter telephone number and convert to the matching pure digital number strings
                        comprehend directly by telephone
    :param: user_input: enter a string of 10 letters telephone number combines with manually entered numbers
    with alphabets
    :precondition: user_input parameter is used to convert into a pure digital number string through the 9-button
    standard
    :post-condition: the parameter will execute its value through a series of translations based on the arrangements
    :return: the translated value for the input users entered for the parameter
    """
    user_input = str(input("Please enter a ten character telephone number(e.g. 800-GET-JUNK)(uppercase for words): "))

    two = "ABC"
    three = "DEF"
    four = "GHI"
    five = "JKL"
    six = "MNO"
    seven = "PQRS"
    eight = "TUV"
    nine = "WXYZ"

    digits_stay_still = str(range(user_input.index(0), user_input.index(2)))
    digits_for_conversion = str(user_input.index(4, 11))

    if random.choice(str(digits_for_conversion)) == random.choice(str(two)):
        Two = "2"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(three)):
        Three = "3"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(four)):
        Four = "4"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(five)):
        Five = "5"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(six)):
        Six = "6"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(seven)):
        Seven = "7"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(eight)):
        Eight = "8"
    elif random.choice(str(digits_for_conversion)) == random.choice(str(nine)):
        Nine = "9"
    elif random.choice(str(digits_stay_still)) == number:
        return digits_stay_still
    elif random.choice(str(user_input)) == "-":
        print("-")
    else:
        return None

    final_result = str(Two), str(Three), str(Four), str(Five), str(Six), str(Seven), str(Eight), str(Nine)

    print(str(random.choice(digits_stay_still)) * 3 + "-" + str(random.choice(final_result)) * 3 + "-"
          + str(random.choice(final_result)) * 4)

number_translator()