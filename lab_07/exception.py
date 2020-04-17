def heron(num: int) -> float:
    """
    Return the square root value of the input.

    :param num: any number inputs by user
    :precondition: num is an integer
    :postcondition: calculate approximate root of num
    :raise ZeroDivisionError: 1 / 0
    :return: square root(in float) of the input
    """

    num_range = range(1, num)
    for i in num_range:
        quotient = (i + num / i) / 2
        result = (quotient + num / quotient) / 2
        squared_result = result ** 2
        if round(squared_result) == num:
            return result
            break
    raise ZeroDivisionError("Zero cannot be divided")

def findAnEvenNumber(input_list: list):
    """
    return even number of the input list
    :precondition: a list of mixed integer number, both odd and even
    :postcondition: the first even number of the list will coming out only
    :param input_list: a list of number randomly placed
    :raise ValueError: if there are no even numbers in the list
    :return: return the first even number of the list
    """
    for i in input_list:
        if i == "," or i == " ":
            pass
        elif int(i) % 2 == 0:
            return i
            break
    raise ValueError("There are only odd numbers")

def main():
    num_input1 = int(input("Please enter a number you want to find the sqrt of: "))
    result = heron(num_input1)
    print(result)
    input_list2 = list(input("Please enter a random list of number: "))
    result1 = findAnEvenNumber(input_list2)
    print(result1)

if __name__ == '__main__':
    main()