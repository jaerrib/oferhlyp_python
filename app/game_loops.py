from app.game import Game


def game_loop():
    game = Game()
    game.active_player = 2
    while not game.game_over:
        game.reset_turn()
        while not game.turn_over:
            turn_loop(game)
    game.board.display_board()
    print("Game Over")


def complete_move(game, move_position, col, row):
    move_col, move_row = move_position[0], move_position[1]
    game.board.data[move_row][move_col] = game.board.data[row][col]
    game.board.data[row][col] = 0


def convert_entry(entered_move):
    # Convert entered move to data usable for comparisons
    move_col = Game.convert_col_to_num(entered_move[0].upper())
    move_row = int(entered_move[1]) - 1
    move_position = (move_col, move_row)
    return move_position


def jump_loop(game, move_position, col, row):
    move_col, move_row = move_position[0], move_position[1]
    jumped_position = game.get_jumped_position(move_col, move_row, col, row)
    jumped_token = game.board.data[jumped_position[1]][jumped_position[0]]
    if jumped_token.player == game.active_player:
        complete_move(game, move_position, col, row)
        game.turn_over = True
    elif jumped_token not in game.jumped_list:
        complete_move(game, move_position, col, row)
        game.jumped_list.append(jumped_token)
        jumped_token.hp -= 1
        if jumped_token.hp == 0:
            game.game_over = jumped_token.is_king
            game.board.data[jumped_position[1]][jumped_position[0]] = 0
        current_position = (move_col, move_row)
        possible_moves = game.get_available_moves(current_position)
        possible_jumps = []
        for position in possible_moves["possible_jumps"]:
            comparison_position = game.get_jumped_position(
                move_col, move_row, position[0], position[1]
            )
            if (
                game.board.data[comparison_position[1]][comparison_position[0]]
                not in game.jumped_list
                and game.board.data[comparison_position[1]][
                    comparison_position[0]
                ].player
                != game.active_player
            ):
                possible_jumps.append(position)
        game.board.display_board()
        if len(possible_jumps) == 0:
            game.turn_over = True
        else:
            moves = {"possible_moves": [], "possible_jumps": possible_jumps}
            print(f"Possible jumps are: {game.get_moves_list(moves)}")
            entered_move = input(
                "Enter row number and col number position to move to or type 'end turn': "
            )
            if entered_move == "end turn":
                game.turn_over = True
            else:
                move_position = convert_entry(entered_move)
                if move_position in possible_moves["possible_jumps"]:
                    jump_loop(
                        game, move_position, current_position[0], current_position[1]
                    )
    else:
        input("invalid selection - Press a <Enter> to continue")


def turn_loop(game):
    game.board.display_board()
    print(f"Player {game.active_player}'s turn")
    selected_token = input(
        "Enter col number and row number of token to move or type 'end turn': "
    )
    if selected_token == "end turn":
        game.turn_over = True
    else:
        col = game.convert_col_to_num(selected_token[0])
        row = int(selected_token[1]) - 1
        # Check if the selected board position contains a token belonging to the player
        if (
            game.board.data[row][col] != 0
            and game.board.data[row][col].player == game.active_player
        ):
            # Then get all the possible moves for that position and let the player enter a move
            possible_moves = game.get_available_moves((col, row))
            print(f"Possible moves/jumps are: {game.get_moves_list(possible_moves)}")
            entered_move = input(
                "Enter row number and col number position to move to: "
            )
            # Convert it to data usable for comparisons
            move_position = convert_entry(entered_move)
            # If the selection is in the list of possible moves, complete the move and change players
            if move_position in possible_moves["possible_moves"]:
                complete_move(game, move_position, col, row)
                game.turn_over = True
            # If the move is a jump, initiate the jumping loop
            if move_position in possible_moves["possible_jumps"]:
                jump_loop(game, move_position, col, row)
        else:
            input("invalid selection - Press a <Enter> to continue")
