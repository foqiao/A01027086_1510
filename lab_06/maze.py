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

def character_first_move():
    global total_length, total_width
    total_length = move_length + min_length
    total_width = move_width + min_width

def user_first_choice():
    global move_length, move_width
    move_length = int(input("Please enter how many steps you want to move horizontally: "))
    move_width = int(input("Please enter how many steps you want to move vertically: "))
    character_first_move()
    total_Length = total_length
    total_Width = total_width
    print("(%d,%d)" % (total_Length, total_Width))

def user_second_choice():
    global move_length1, move_width1
    move_length1 = int(input("Please enter how many steps you want to move horizontally: "))
    move_width1 = int(input("Please enter how many steps you want to move vertically: "))
    total_Length = move_length1 + total_length
    total_Width = move_width1 + total_width
    print("(%d,%d)" % (total_Length, total_Width))

def user_choice():
    global move_length1, move_width1
    move_length1 = int(input("Please enter how many steps you want to move horizontally: "))
    move_width1 = int(input("Please enter how many steps you want to move vertically: "))
    total_Length = move_length1 + total_length
    total_Width = move_width1 + total_width
    print("(%d,%d)" % (total_Length, total_Width))

def character_second_move():
    global total_LENGTH, total_WIDTH
    total_LENGTH = move_length1 + total_length
    total_WIDTH = move_width1 + total_width

def first_valid_move(userBoard, userCharacter):
    user_first_choice()
    if length > total_length > 0:
        if width > total_width > 0:
            pass

def valid_move(userBoard, userCharacter):
    user_choice()
    if length > total_length > 0:
        if width > total_width > 0:
            pass
        else:
            game()

def check_if_exit_reached():
    current_position = total_length * total_width
    final_exit = length * width
    if current_position >= final_exit:
        print("You Win")

def game():
    user_first_choice()
    character_first_move()
    while not check_if_exit_reached():
        first_valid_move(board, character_first_move)
        if first_valid_move:
            check_if_exit_reached()
            game1()
        else:
            print("invalid")
            game()

def game1():
    user_choice()
    while not check_if_exit_reached():
        valid_move(board, character_first_move)
        if valid_move:
            check_if_exit_reached()
        else:
            print("invalid")
            game1()

def main():
    board()
    game()

def main1():
    game1()

if __name__ == '__main__':
    main()
    main1()