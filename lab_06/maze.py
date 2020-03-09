from numpy import NaN

def make_board():
    global length, width
    length = 5
    width = 5
    print("The board is (%d,%d)" % (length, width))

def make_character(next_step):
    global current_y, current_x
    current_x = {}
    current_y = {}
    i = len(current_x)
    j = len(current_y)
    if next_step == "up":
        current_y[j].append(j + 1)
        print("(%d,%d)" % (current_x[i], current_y[j]))
    elif next_step == "left":
        current_x[i].append(i + 1)
        print("(%d,%d)" % (current_x[i], current_y[j]))
    elif next_step == "right":
        current_x[i].append(i + 1)
        print("(%d,%d)" % (current_x[i], current_y[j]))
    elif next_step == "down":
        current_y[i].append(j + 1)
        print("(%d,%d)" % (current_x[i], current_y[j]))

def validate_move(next_step):
    global current_y, current_x
    i = len(current_x)
    j = len(current_y)
    if current_x[i] < 0 or current_y[j] < 0:
        print("invalid")
        make_character(next_step)
    elif next_step == NaN:
        print("invalid")
        make_character(next_step)
    elif len(current_y) == 0 or len(current_x) == 0:
        if next_step == "up":
            print("invalid")
            make_character(next_step)
        elif next_step == "left":
            print("invalid")
            make_character(next_step)
        else:
            make_character(next_step)

def check_if_exit_reached():
    global current_x, current_y
    if len(current_x) * len(current_y) >= 16:
        print("You Win")

def game():
    make_board()
    found_exit = False
    while not found_exit:
        next_step1 = str(input("Do you want to go up, down, right or left? Please enter: "))
        make_character(next_step1)
        validate_move(next_step1)
        if validate_move:
            check_if_exit_reached()
        else:
            make_character(next_step1)

if __name__ == '__main__':
    game()