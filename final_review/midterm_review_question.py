import string


def number(num):
    return num * 3

def kilo_to_inch(kilo):
    return float(kilo) * 39370.1

def average(num1, num2, num3):
    average_num = (int(num1) + int(num2) + int(num3)) / 3
    return float(average_num)

def best_grade(grade1, grade2, grade3, grade4):
    if 0 <= int(grade1) <= 100 and 0 <= int(grade2) <= 100 and 0 <= int(grade3) <= 100 and 0 <= int(grade4) <= 100:
        grade_rank = []
        grade_rank.append(grade1)
        grade_rank.append(grade2)
        grade_rank.append(grade3)
        grade_rank.append(grade4)
        grade_rank.sort(reverse=True)
        for i in range(0, 3):
            return i

def choice():
    x = 3
    y = 12.5
    multiple = x * y
    return "The rabbit is " + str(x)
    return "The rabbit is " + str(x) + " years old"
    return str(y) + " is average"
    return str(x) + " * " + str(y) + " is " + str(multiple)

def total_length(s1, s2):
    return len(s1) + len(s2)

def boolean_expression(empty, full):
    if empty is True or full is True:
        return True
    else:
        return False

def boolean_expression1(a, b):
    if a != b:
        return True
    else:
        return False

def land_density(population, land_size):
    if 10 < int(population) < 35:
        population *= 1000000
        density = population / land_size
        if density > 100:
            return "Densely populated."

def acidity(pH):
    if int(pH) < 3:
        return "%s is acidity! Be careful" % pH
    else:
        return "%s is acid" % pH

def first_ocurrance(character):
    alpha = string.ascii_letters
    for i in enumerate(alpha):
        if i == character[0]:
            return i
        else:
            return -1

def times_occurance(letter):
    alpha = string.ascii_letters
    return alpha.count(letter)

def four_digit_id():
    num = [4353, 2314, 2956, 3382, 9362, 3900]
    num.remove(num[3])
    num.index(9362)
    num.insert(-2, 4499)
    num.append(5566)
    num.append(1830)
    num.sort(reverse=True)
    num.sort()
    return num

def appointment():
    list_appointment = ['9:00', '9:30', '14:00', '15:00', '15:30']
    list_appointment.append('16:30')
    str(list_appointment) + '16:30'
    return str(list_appointment)

def letter_triangle():
    letter = "T"
    for i in range(0, 7):
        return i
        if i / 1 >= 1:
           return i * letter

def main():
    num = input("please enter a number: ")
    print(number(num))

    kilo = input("Please enter a weight in kilo: ")
    print(kilo_to_inch(kilo))

    num1 = input("Please enter a number: ")
    num2 = input("Please enter another number: ")
    num3 = input("Plaese enter another number: ")
    print(average(num1, num2, num3))

    grade1 = input("Please enter first grade: ")
    grade2 = input("Please enter second grade: ")
    grade3 = input("Please enter third grade: ")
    grade4 = input("Please enter fourth grade: ")
    print(best_grade(grade1, grade2, grade3, grade4))

    print(choice())

    s1 = input("Please enter a string: ")
    s2 = input("Please enter another string: ")
    print(total_length(s1, s2))

    empty = True
    full = False
    print(boolean_expression(empty, full))

    a = 1
    b = 2
    print(boolean_expression1(a, b))

    population = input("Please input a nation's population: ")
    land_size = input("Please input a nation's land mass: ")
    print(land_density(population, land_size))

    pH = input("Please input a pH value: ")
    print(acidity(pH))

    character = input("Please enter an English character: ")
    first_occur = first_ocurrance(character)
    print(first_occur)

    letter = input("Please enter a single letter: ")
    times_occur = times_occurance(letter)
    print(times_occur)

    print(four_digit_id())

    print(appointment())



if __name__ == '__main__':
    main()