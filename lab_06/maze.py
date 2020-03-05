def game():
    board()
    found_exit = False
    while not found_exit:
        user_choice()
        valid_move(board, character)
        if valid_move:
            character()
            check_if_exit_reached()
        else:
            game()

def board():
    length = 5
    min_length = 0
    width = 5
    min_width = 0
    print("The board is %d * %d." % (length, length))
    print("The minimum coordinate is (%d,%d)." % (min_length, min_width))
    print("The maximum coordinate is (%d,%d)." % (length, width))

def character():
    user_choice()
    moving_log = {}
    steps = range(0, 25)
    for i in steps:
        moving_log.update({i: "(%d,%d)" % (move_length, move_width)})
        total_length = move_length + moving_log[i][1]
        total_width = move_width + moving_log[i][3]
        print("(%d,%d)" % (total_length, total_width))

def user_choice():
    move_length = int(input("Please enter how many steps you want to move horizontally: "))
    move_width = int(input("Please enter how many steps you want to move vertically: "))

def valid_move(userBoard, userCharacter):
    character()
    if length > total_length > 0:
        if width > total_width > 0:
            pass

def check_if_exit_reached():
    current_position = total_length * total_width
    final_exit = length * width
    if current_position >= final_exit:
        print("You Win")
    else:
        print("More steps needed to reach the exit.")

if __name__ == '__main__':
    game()