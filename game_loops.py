from game import Game


def game_loop():
    game = Game()
    game.active_player = 2
    while not game.game_over:
        game.reset_turn()
        while not game.turn_over:
            turn_loop(game)
    game.board.display_board()
    print("Game Over")


def complete_move(game, move_col, move_row, col, row):
    game.board.data[move_row][move_col] = game.board.data[row][col]
    game.board.data[row][col] = 0


def jump_loop(game, move_position, col, row, possible_moves):
    move_col, move_row = move_position[0], move_position[1]
    jump_index = possible_moves["possible_jumps"].index(move_position)
    jumped_token = possible_moves["jumpable"][jump_index]
    print("In list?", jumped_token in game.jumped_list)

    if (
        game.board.data[jumped_token[1]][jumped_token[0]].player != game.active_player
    ) and jumped_token not in game.jumped_list:
        game.board.data[move_row][move_col] = game.board.data[row][col]
        game.board.data[row][col] = 0
        game.board.data[jumped_token[1]][jumped_token[0]].hp -= 1
        game.jumped_list.append(game.board.data[jumped_token[1]][jumped_token[0]])
        if game.board.data[jumped_token[1]][jumped_token[0]].hp == 0:
            game.game_over = game.board.data[jumped_token[1]][jumped_token[0]].is_king
            game.board.data[jumped_token[1]][jumped_token[0]] = 0
    elif (
        game.board.data[jumped_token[1]][jumped_token[0]].player == game.active_player
        and jumped_token not in game.jumped_list
    ):
        game.board.data[move_row][move_col] = game.board.data[row][col]
        game.board.data[row][col] = 0
        game.turn_over = True
    else:
        input("invalid selection - Press a <Enter> to continue")


def turn_loop(game):
    game.board.display_board()
    print(game.jumped_list)
    print(f"Player {game.active_player}'s turn")
    selected_token = input(
        "Enter col number and row number of token to move or type 'end turn': "
    )
    if selected_token == "end turn":
        game.turn_over = True
    else:
        col = game.convert_col_to_num(selected_token[0])
        row = int(selected_token[1]) - 1
        if (
            game.board.data[row][col] != 0
            and game.board.data[row][col].player == game.active_player
        ):
            possible_moves = game.get_available_moves((col, row))
            print(f"Possible moves/jumps are: {game.get_moves_list(possible_moves)}")
            entered_move = input(
                "Enter row number and col number position to move to: "
            )
            move_col = game.convert_col_to_num(entered_move[0].upper())
            move_row = int(entered_move[1]) - 1
            move_position = (move_col, move_row)
            if move_position in possible_moves["possible_moves"]:
                complete_move(game, move_col, move_row, col, row)
                game.turn_over = True
            if move_position in possible_moves["possible_jumps"]:
                jump_loop(game, move_position, col, row, possible_moves)
        else:
            input("invalid selection - Press a <Enter> to continue")
