import random

def grade(first_grade, second_grade, third_grade, fourth_grade, fifth_grade):
  grade_list = [first_grade, second_grade, third_grade, fourth_grade, fifth_grade]
  grade_list.sort()
  print(grade_list)

def my_id():
    my_id_string = [4353, 2314, 2956, 3382, 9362, 3900]

    my_id_string.remove(3382)
    my_id_string.index(9362)
    my_id_string.append(4499)
    my_id_string.append(5566)
    my_id_string.append(1830)
    my_id_string.reverse()
    my_id_string.sort()

    print(my_id_string)

if __name__ == '__main__':
    random_first_grade = random.randint(0, 100)
    random_second_grade = random.randint(0, 100)
    random_third_grade = random.randint(0, 100)
    random_fourth_grade = random.randint(0, 100)
    random_fifth_grade = random.randint(0, 100)
    grade(random_first_grade, random_second_grade, random_third_grade, random_fourth_grade, random_fifth_grade)

    my_id()