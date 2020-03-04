def game():
    found_exit = exit()
    while not found_exit:
        board()
        character()
        user_choice()
        valid_move(board, character, user_choice)
        if valid_move:
            user_choice()
            check_if_exit_reached()
        else:
            move_length = int(input("Your move isn't valid, please re-enter one: "))
            game()

def board():
    length = 5
    board_size = length ** 2
    return board_size

def character():
    characterX = 0
    characterY = 0
    character_position = characterX * characterY
    return character_position

def user_choice():
    move_length = int(input("Please enter how far you want to go: "))
    character_location = character()
    character_location += move_length
    return character_location

def valid_move(board_setup, character_input, user_choice_input):
    board_setup = board()
    character_input = character()
    user_choice_input = user_choice()

    total_movement = character_input + user_choice_input

    if total_movement <= board_setup:
        user_choice()

total_movement_check = character() + user_choice()

def check_if_exit_reached():
    if total_movement_check >= 25:
        print("Winner")
    else:
        print("Still more to go")

def main():
    game()

if __name__ == '__main__':
    main()