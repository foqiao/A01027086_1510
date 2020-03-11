def board():
    """
    length: specify the length of the 5 * 5 board
    :return: the board's size is returned to the user
    """
    length = range(0, 5)
    board_size = "(%d,%d)" % (max(length), max(length))
    print(board_size)

def character():
    """
    x_location: the initial location of the character compares to x-axis
    y_location: the initial location of the character compares to y-axis
    :return: the position of the character in first round
    """
    global x_location, y_location
    x_location = 0
    y_location = 0
    choice()

def current_character():
    """
    x_location: the location the character current located after first round to x-axis
    y_location: the location the character current located after first round to y-axis
    :return: the position of the character in second round
    """
    global x_location, y_location
    print(f"{x_location},{y_location}")

def choice():
    """
    location: choose the next step for character to move on
    :return: the updated position of the character after choosing the next step
    """
    global x_location, y_location, location
    location = str(input("Which direction do you want to go(up, down, right or left): "))
    validate_move()
    if location == "up":
        y_location -= 1
        print(x_location)
    elif location == "down":
        y_location += 1
    elif location == "right":
        x_location += 1
    elif location == "left":
        x_location -= 1
    print("(%d,%d)" % (x_location, y_location))

def validate_move():
    """
    to see whether the move from choice is valid
    :return: the approval of the move from the character
    """
    global x_location, y_location, location
    if x_location == 0 or y_location == 0:
        if location == "up":
            print("invalid")
            choice()
        elif location == "left":
            print("invalid")
            choice()
    else:
        pass

def last_step():
    """
    whether the character reaches the exit
    :return: Win or more to go
    """
    global x_location, y_location
    if x_location == 4 and y_location == 4:
        pass
    else:
        print("You are still a long way to go")
        choice()

def game():
    board()
    character()
    validate_move()
    if validate_move:
        current_character()
        last_step()
        if last_step:
            print("You Win")
        else:
            game()
    else:
        game1()

def game1():
    choice()
    validate_move()
    if validate_move:
        current_character()
        last_step()
        game1()
    else:
        game1()

if __name__ == '__main__':
    game()
    game1()