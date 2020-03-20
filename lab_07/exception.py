from numpy import NaN


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

def findAnEvenNumber(input_list: list):
    """
    return even number of the input list
    :precondition: a list of mixed integer number, both odd and even
    :postcondition: the even number will coming out only while odd are left behind
    :param input_list: a list of number randomly placed
    :raise ValueError: if there are no even numbers in the list
    :return: return even number of the list
    """
    for i in input_list:
        if int(i) % 2 == 0:
            print(i)
            break

try:
    input_list1 = [3]
except ValueError:
    print("No, It's an odd number!")

def main():
    num_input1 = int(input("Please enter a number you want to find the sqrt of: "))
    heron(num_input1)
    input_list2 = list(input("Please enter a random list of number: "))
    findAnEvenNumber(input_list2)

if __name__ == '__main__':
    main()