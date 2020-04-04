def number(num):
    return num * 3

def kilo_to_inch(kilo):
    return kilo * 39370.1

def average(num1, num2, num3):
    average_num = (num1 + num2 + num3) / 3
    return float(average_num)

def best_grade(grade1, grade2, grade3, grade4):
    if 0 <= grade1 <= 100 and 0 <= grade2 <= 100 and 0 <= grade3 <= 100 and 0 <= grade4 <= 100:
        grade_rank = []
        grade_rank.append(grade1, grade2, grade3, grade4)
        grade_rank.sort(reverse=True)
        for i in range(0, 3):
            return i

def choice():
    x = 3
    y = 12.5
    multiple = x * y
    return "The rabbit is " + x
    return "The rabbit is " + x + " years old"
    return y + " is average"
    return x + " * " + y + " is " + multiple

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
    if 10 < population < 35:
        population *= 1000000
        density = population / land_size
        if density > 100:
            return "Densely populated."

