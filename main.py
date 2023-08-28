from game import Game


def convert_col_to_num(character):
    letters = "ABCDEFG"
    for index in range(0, len(letters)):
        if character == letters[index]:
            return index


def convert_num_to_letter(num):
    letters = "ABCDEFG"
    return letters[num - 1]


def display_moves(move_list):
    converted_list = []
    for position in move_list["possible_moves"]:
        if position is not None:
            col = convert_num_to_letter(position[0] + 1)
            row = str(position[1] + 1)
            converted_list.append(col+row)
    for position in move_list["possible_jumps"]:
        if position is not None:
            col = convert_num_to_letter(position[0] + 1)
            row = str(position[1] + 1)
            converted_list.append(col+row)
    print(f"Possible moves/jumps are: {converted_list}")


def change_player(active_player):
    if active_player == 1:
        return 2
    elif active_player == 2:
        return 1


def game_loop():
    my_game = Game()
    game_over = False
    active_player = 2
    while not game_over:
        jumped_list = []
        turn_over = False
        active_player = change_player(active_player)
        while not turn_over:
            my_game.board.display_board()
            print(jumped_list)
            print(f"Player {active_player}'s turn")
            selected_token = (input(
                "Enter col number and row number of token to move or type 'end turn': "))
            if selected_token == "end turn":
                turn_over = True
            else:
                col = convert_col_to_num(selected_token[0].upper())
                row = int(selected_token[1]) - 1
                if (my_game.board.data[row][col] != 0 and
                        my_game.board.data[row][col].player == active_player):
                    possible_moves = my_game.get_available_moves((col, row))
                    display_moves(possible_moves)
                    entered_move = (input(
                        "Enter row number and col number position to move to: "))
                    move_col = convert_col_to_num(entered_move[0].upper())
                    move_row = int(entered_move[1]) - 1
                    move_position = (move_col, move_row)
                    if move_position in possible_moves["possible_moves"]:
                        my_game.board.data[move_row][move_col] = (
                            my_game.board.data)[row][col]
                        my_game.board.data[row][col] = 0
                        turn_over = True
                    if move_position in possible_moves["possible_jumps"]:
                        jump_index = (
                            possible_moves["possible_jumps"].index(move_position))
                        jumped_token = possible_moves["jumpable"][jump_index]
                        print("In list?", jumped_token in jumped_list)

                        if (my_game.board.data[jumped_token[1]][jumped_token[0]].player
                                != active_player) and jumped_token not in jumped_list:
                            my_game.board.data[move_row][move_col] = (
                                my_game.board.data)[row][col]
                            my_game.board.data[row][col] = 0
                            my_game.board.data[jumped_token[1]][jumped_token[0]].hp -= 1
                            jumped_list.append(my_game.board.data[jumped_token[1]][jumped_token[0]])
                            if (my_game.board.data[jumped_token[1]][jumped_token[0]].hp
                                    == 0):
                                game_over = my_game.board.data[jumped_token[1]][jumped_token[0]].is_king
                                my_game.board.data[jumped_token[1]][jumped_token[0]] = 0
                        elif my_game.board.data[jumped_token[1]][jumped_token[0]].player == active_player and jumped_token not in jumped_list:
                            my_game.board.data[move_row][move_col] = (
                                my_game.board.data)[row][col]
                            my_game.board.data[row][col] = 0
                            turn_over = True
                        else:
                            print("invalid selection")
                else:
                    print("invalid selection")
    my_game.board.display_board()
    print("Game Over")


game_loop()
