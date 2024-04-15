from game import Game


def game_loop():
    my_game = Game()
    my_game.active_player = 2
    while not my_game.game_over:
        jumped_list = []
        my_game.turn_over = False
        my_game.change_player()
        while not my_game.turn_over:
            my_game.board.display_board()
            print(jumped_list)
            print(f"Player {my_game.active_player}'s turn")
            selected_token = input(
                "Enter col number and row number of token to move or type 'end turn': "
            )
            if selected_token == "end turn":
                my_game.turn_over = True
            else:
                col = my_game.convert_col_to_num(selected_token[0])
                row = int(selected_token[1]) - 1
                if (
                    my_game.board.data[row][col] != 0
                    and my_game.board.data[row][col].player == my_game.active_player
                ):
                    possible_moves = my_game.get_available_moves((col, row))
                    print(
                        f"Possible moves/jumps are: {my_game.get_moves_list(possible_moves)}"
                    )
                    entered_move = input(
                        "Enter row number and col number position to move to: "
                    )
                    move_col = my_game.convert_col_to_num(entered_move[0].upper())
                    move_row = int(entered_move[1]) - 1
                    move_position = (move_col, move_row)
                    if move_position in possible_moves["possible_moves"]:
                        my_game.board.data[move_row][move_col] = my_game.board.data[
                            row
                        ][col]
                        my_game.board.data[row][col] = 0
                        my_game.turn_over = True
                    if move_position in possible_moves["possible_jumps"]:
                        jump_index = possible_moves["possible_jumps"].index(
                            move_position
                        )
                        jumped_token = possible_moves["jumpable"][jump_index]
                        print("In list?", jumped_token in jumped_list)

                        if (
                            my_game.board.data[jumped_token[1]][jumped_token[0]].player
                            != my_game.active_player
                        ) and jumped_token not in jumped_list:
                            my_game.board.data[move_row][move_col] = (
                                my_game.board.data
                            )[row][col]
                            my_game.board.data[row][col] = 0
                            my_game.board.data[jumped_token[1]][jumped_token[0]].hp -= 1
                            jumped_list.append(
                                my_game.board.data[jumped_token[1]][jumped_token[0]]
                            )
                            if (
                                my_game.board.data[jumped_token[1]][jumped_token[0]].hp
                                == 0
                            ):
                                my_game.game_over = my_game.board.data[jumped_token[1]][
                                    jumped_token[0]
                                ].is_king
                                my_game.board.data[jumped_token[1]][jumped_token[0]] = 0
                        elif (
                            my_game.board.data[jumped_token[1]][jumped_token[0]].player
                            == my_game.active_player
                            and jumped_token not in jumped_list
                        ):
                            my_game.board.data[move_row][move_col] = (
                                my_game.board.data
                            )[row][col]
                            my_game.board.data[row][col] = 0
                            my_game.turn_over = True
                        else:
                            print("invalid selection")
                else:
                    print("invalid selection")
    my_game.board.display_board()
    print("Game Over")


game_loop()
