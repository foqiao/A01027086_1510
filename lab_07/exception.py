def heron(num: int) -> float:
    """
    return the square root value of the input
    :precondition: a number without perfect root
    :postcondition: a number with an approximate root
    :param num: any number inputs by user
    :return: square root(in float) of the input
    """
    num_range = range(1, num)
    for number in num_range:
        quotient = (number + num / number) / 2
        result = (quotient + num / quotient) / 2
        if round(result ** 2) == num:
            print(result)
            break

try:
    heron(1 / 0)
except ZeroDivisionError:
    print("No, I can't do it!")

num_input = int(input("Please enter a number you want to find the sqrt of: "))
heron(num_input)

def findAnEvenNumber(num1: list):
    """
    return first even value of the list
    :param num1: a list of numbers ready to inspect by the function
    :precondition: a list of random numbers, whatever user input, an odd/even mixed string
    :postcondition: return the first even number of the list
    :raise ValueError: the number that isn't even
    :return: the number has qualified by the function
    """
    for i in range(0, len(num1)):
        if num1[i] % 2 == 0:
            print(i)
            break

try:
    list_num = [1, 3]
    findAnEvenNumber(list_num)
except ValueError:
    print("Sorry, it isn't an even number!")

num1_input = list(input("Please enter a list of number: "))
findAnEvenNumber(num1_input)