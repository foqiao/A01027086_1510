def heron(num: int) -> float:
    """
    Return the square root value of the input.

    :param num: any number inputs by user
    :precondition: num is an integer
    :postcondition: calculate approximate root of num
    :raise ZeroDivisionError: 1 / 0
    :return: square root(in float) of the input

    >>> 42
    6.4843283582089555
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
                num = 0
            except ZeroDivisionError:
                print("No, I can't do that!")
                print(-1)

def findAnEvenNumber(input_list: list):
    """
    return even number of the input list
    :precondition: a list of mixed integer number, both odd and even
    :postcondition: the first even number of the list will coming out only
    :param input_list: a list of number randomly placed
    :raise ValueError: if there are no even numbers in the list
    :return: return the first even number of the list

    >>> 1,2,3
    3
    """
    for i in input_list:
        if i == "," or i == " ":
            pass
        elif int(i) % 2 == 0:
            print(i)
            break
            try:
                input_list = [3]
            except ValueError:
                print("No, It's an odd number!")

def main():
    num_input1 = int(input("Please enter a number you want to find the sqrt of: "))
    heron(num_input1)
    input_list2 = list(input("Please enter a random list of number: "))
    findAnEvenNumber(input_list2)

if __name__ == '__main__':
    main()