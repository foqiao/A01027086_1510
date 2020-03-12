def make_board(length: int, width: int) -> dict:
    """
    length: specify the length of the 5 * 5 board
    :return: the board's size is returned to the user
    """
    board_size = {'length': length, 'width': width}
    return board_size

def make_character(x_location: int, y_location: int) -> dict:
    """
    x_location: the initial location of the character compares to x-axis
    y_location: the initial location of the character compares to y-axis
    :return: the position of the character in first round
    """
    character_dict = {'x': x_location, 'y': y_location}
    print(character_dict)
    return character_dict

def get_user_choice():
    """
    location: choose the next step for character to move on
    :return: the updated position of the character after choosing the next step
    """
    direction = str(input("Which direction do you want to go(up, down, right or left): "))
    return direction

def validate_move(board, character, direction):
    """
    to see whether the move from choice is valid
    :return: the approval of the move from the character
    """
    direction_list = ["left", "right", "up", "down"]
    if direction not in direction_list:
        return False
    if character.get('x') == 0:
        if direction == "left":
            return False
    if character.get('y') == 0:
        if direction == "up":
            return False
    if character.get('x') == board.get('length') - 1:
        if direction == "right":
            return False
    if character.get('y') == board.get('width') - 1:
        if direction == "down":
            return False

    return True

def last_step(board, character):
    """
    whether the character reaches the exit
    :return: Win or more to go
    """
    if character['x'] == board.get('length') - 1 and character['y'] == board.get('width') - 1:
        print("You Win")
    else:
        print("You are still a long way to go")

def move_character(character: dict, direction: str):
    if direction == "up":
        character['y'] -= 1
    if direction == "down":
        character['y'] += 1
    if direction == "right":
        character['x'] += 1
    if direction == "left":
        character['x'] -= 1

    print(character)

def game():
    board = make_board(5, 5)
    character = make_character(0, 0)
    found_exit = False
    while not found_exit:
        direction = get_user_choice()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            move_character(character, direction)
            last_step(board, character)
        else:
            print("invalid")

if __name__ == '__main__':
    game()