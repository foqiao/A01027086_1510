from numpy import NaN

def board():
    global length, width
    length = 5
    min_length = 0
    width = 5
    min_width = 0
    print("The board is %d * %d." % (length, width))
    print("The minimum coordinate is (%d,%d)." % (min_length, min_width))
    print("The maximum coordinate is (%d,%d)." % (length, width))
    print("You current position is (%d,%d)." % (min_length, min_width))

def user_choice():
    global move_length, move_width
    move_length = int(input("Please enter how many steps you want to move horizontally: "))
    move_width = int(input("Please enter how many steps you want to move vertically: "))

def character():
    global move_length, move_width
    length_log = []
    width_log = []
    length_log.append(move_length)
    width_log.append(move_width)
    for i in (0, len(length_log) - 1):
        for j in (0, len(width_log) - 1):
            move_length *= length_log[i]
            move_width *= width_log[j]
    print("(%d,%d)" % (move_length, move_width))

def valid_move(board1, user_choice1):
    if user_choice1 > board1:
        print("invalid")
        user_choice()
    elif user_choice1 < board1:
        pass
    elif user_choice1 == NaN:
        print("try again")
        user_choice()

def check_if_exit_reached():
    current_position = move_length * move_width
    final_exit = length * width
    if current_position >= final_exit:
        print("You Win")

def game1():
    user_choice()
    character()
    check_if_exit_reached()
    while not check_if_exit_reached:
        valid_move(board, user_choice)
        if valid_move:
            check_if_exit_reached()
            game1()
        else:
            game1()

def game():
    board()
    game1()

if __name__ == '__main__':
    game()
    game1()