def heron(num: int) -> float:
    """
    return the square root value of the input
    :precondition: a number without perfect root
    :postcondition: a number with an approximate root
    :param num: any number inputs by user
    :raise ZeroDivisionError: 1 / 0
    :return: square root(in float) of the input
    """
    num_range = range(-num, num)
    for number in num_range:
        quotient = (number + num / number) / 2
        result = (quotient + num / quotient) / 2
        if round(result ** 2) == num:
            print(result)
            break

num_input = int(input("Please enter a number you want to find the sqrt of: "))
heron(num_input)

def findAnEvenNumber(num2: list):
    """
    return first even value of the list
    :param num2: a list of numbers ready to inspect by the function
    :precondition: a list of random numbers, whatever user input, an odd/even mixed string
    :postcondition: return the first even number of the list
    :raise ValueError: the number that isn't even
    :return: the number has qualified by the function
    """
    for i in num2:
        if i % 2 == 0:
            return i
    raise ValueError

num1_input = list(input("Please enter a list of number: "))
findAnEvenNumber(num1_input)
