def format_name(first_name, last_name):
    cap_first_name = first_name.title()
    cap_last_name = last_name.title()
    print("Hello, you are " + cap_first_name.lstrip() + " " + cap_last_name.rstrip())

def tripleR(string):
    result = string * 3

    print(str(result))

def this_year(pos_int):
    if pos_int == 2:
        return_integer = pos_int * 1000 + pos_int * 10
        print(return_integer)
    else:
        return None

if __name__ == '__main__':
    first_name1 = str(input("Please enter your first_name: "))
    last_name1 = str(input("Please enter your last_name: "))
    format_name(first_name1, last_name1)

    string1 = str(input("Please enter a string of letter: "))
    tripleR(string1)

    pos_int1 = int(input("Please specify a positive integer: "))
    this_year(pos_int1)