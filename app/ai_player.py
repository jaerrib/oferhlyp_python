import random

from app.game_loops import (
    select_token,
    assign_selected,
    assign_jump,
    turn_reset,
    get_check_positions,
)


def play_computer_move(data):
    # Choose a token to move
    token_list = []
    for row in range(0, 7):
        for col in range(0, 7):
            if data["board"][row][col] != 0 and data["board"][row][col]["player"] == 2:
                possible_moves = get_moves(data, (col, row))
                if (
                    len(possible_moves["possible_moves"]) > 0
                    or len(possible_moves["possible_jumps"]) > 0
                ):
                    token_list.append((col, row))
    selected_token = random.choice(token_list)
    data = select_token(data, row=selected_token[1], col=selected_token[0])
    # Determine moves available for that token
    possible_moves = get_moves(data, selected_token)
    # move_choices = []
    move_choices = [
        item
        for sublist in possible_moves.values()
        if sublist != possible_moves["jumpable"]
        for item in sublist
    ]
    selected_move = random.choice(move_choices)
    # Choose a move to play for that token
    if (
        selected_move
        in possible_moves["possible_moves"]
        # and data["actively_jumping"] == False
    ):
        data = assign_selected(data, row=selected_move[1], col=selected_move[0])
        data = turn_reset(data)
    elif selected_move in possible_moves["possible_jumps"]:
        data = assign_jump(
            data,
            selected_move,
            col=data["active_col"],
            row=data["active_row"],
        )
        data = turn_reset(data)  # remove after implementing continued jumping
    # If jumping, decide whether to continue
    # (
    #     play_computer_move(data)
    #     if data["actively_jumping"] and random.random() < 0.2
    #     else turn_reset(data)
    # )
    return data


def get_moves(data, pos_tuple):
    possible_moves = []
    possible_jumps = []
    jumpable = []
    if data["board"][pos_tuple[1]][pos_tuple[0]] != 0:
        position_dict = get_check_positions(pos_tuple)
        for index in range(0, 8):
            col = position_dict["adjacent"][index][0]
            row = position_dict["adjacent"][index][1]
            x_col = position_dict["extended"][index][0]
            x_row = position_dict["extended"][index][1]
            if not is_outside(pos_tuple=(col, row)) and data["board"][row][col] == 0:
                possible_moves.append(position_dict["adjacent"][index])
            elif (
                not is_outside((x_col, x_row))
                and data["board"][x_row][x_col] == 0
                and data["board"][x_row][x_col] not in data["jumped_list"]
            ):
                possible_jumps.append(position_dict["extended"][index])
                jumpable.append(position_dict["adjacent"][index])
    available_moves = {
        "possible_moves": possible_moves,
        "possible_jumps": possible_jumps,
        "jumpable": jumpable,
    }
    return available_moves


def is_outside(pos_tuple):
    board_size = 7
    return not 0 <= pos_tuple[0] < board_size or not 0 <= pos_tuple[1] < board_size
