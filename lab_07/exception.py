def heron(num: int) -> float:
    """
    return the square root value of the input
    :precondition: a number without perfect root
    :postcondition: a number with an approximate root
    :param num: any number inputs by user
    :raise ZeroDivisionError: 1 / 0
    :return: square root(in float) of the input
    """
    num_range = range(1, num)
    for i in num_range:
        quotient = (i + num / i) / 2
        result = (quotient + num / quotient) / 2
        squared_result = result ** 2
        if round(squared_result) == num:
            print(result)
            break

try:
    num_input = 0
except ZeroDivisionError:
    print("No, I can't do that!")
    print(-1)

num_input1 = int(input("Please enter a number you want to find the sqrt of: "))
heron(num_input1)

def findAnEvenNumber(input_list: list):
    for i in input_list:
        if i % 2 == 0:
            print(i)

input_list2 = list(input("Please enter a random list of number: "))
findAnEvenNumber(input_list2)

try:
    input_list1 = [3]
except ValueError:
    print("No, It's an odd number!")