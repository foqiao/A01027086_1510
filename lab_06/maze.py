def game():
    board()
    character()
    found_exit = False
    while not found_exit:
        valid_move(board, character, user_choice)
        if valid_move:
            user_choice()
            check_if_exit_reached()
        else:
            move_length = int(input("Your move isn't valid, please re-enter one: "))
            user_choice()

def board():
    length = 5
    min_length = 0
    width= 5
    min_width = 0
    print("The board is %d * %d." % (length, length))
    print("The minimum coordinate is (%d,%d)." % (min_length, min_width))
    print("The maximum coordinate is (%d,%d)." % (length, width))

def character():
    user_choice()
    if 0 <= move_length <= 5:
        if 0 <= move_width <= 5:
            location = "Your are (%d,%d) from previous location." % (move_length, move_width)
            return str(location)

def user_choice():
    move_length = int(input("Please enter how many steps you want to move horizontally: "))
    move_width = int(input("Please enter how many steps you want to move vertically: "))
    moving_log = {}
    steps = range(0, 25)
    for i in steps:
        moving_log.update({ i: "(%d,%d)" % (move_length, move_width) })
        steps.pop(i)
        return moving_log[i]

def valid_move(board_input, character_input, user_choice_input):
    

if __name__ == '__main__':
    game()