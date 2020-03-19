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
        if result ** 2 == num:
            print(result)

num_input = int(input("Please enter a number you want to find the sqrt of: "))
heron(num_input)