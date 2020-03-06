def board():
    global length, width, min_length, min_width
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
    total_Length = move_length + total_length
    total_Width = move_width + total_width
    print("(%d,%d)" % (total_Length, total_Width))

def character():
    global total_length, total_width
    total_length = move_length + min_length
    total_width = move_width + min_width
    print("(%d,%d)" % (total_length, total_width))

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

def game():
    board()
    character()
    while not check_if_exit_reached():
        valid_move(board, character)
        if valid_move:
            check_if_exit_reached()
            if check_if_exit_reached:
                print("You win")
            else:
                print("You haven't win yet.")

if __name__ == '__main__':
    game()