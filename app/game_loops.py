def assign_jump(data, move_position, col, row):
    move_col, move_row = move_position[0], move_position[1]
    jumped_position = get_jumped_position(move_col, move_row, col, row)
    jumped_token = data["board"][jumped_position[1]][jumped_position[0]]
    if jumped_token["player"] == data["active_player"]:
        data = assign_selected(data, move_row, move_col)
        turn_reset(data)
        return data
    elif jumped_position not in data["jumped_list"]:
        data = assign_selected(data, move_row, move_col)
        data["jumped_list"].append(jumped_position)
        jumped_token["hp"] -= 1
        if jumped_token["hp"] == 0:
            data["game_over"] = jumped_token["is_king"]
            data["board"][jumped_position[1]][jumped_position[0]] = 0
        current_position = (move_col, move_row)
        possible_moves = get_available_moves(data, current_position)
        possible_jumps = []
        for position in possible_moves["possible_jumps"]:
            comparison_position = get_jumped_position(
                move_col, move_row, position[0], position[1]
            )
            if (
                data["board"][comparison_position[1]][comparison_position[0]]
                not in data["jumped_list"]
                and data["board"][comparison_position[1]][comparison_position[0]][
                    "player"
                ]
                != data["active_player"]
            ):
                possible_jumps.append(position)
        if len(possible_jumps) == 0:
            turn_reset(data)
            data["actively_jumping"] = False
        else:
            data["actively_jumping"] = True
            data["active_row"] = current_position[1]
            data["active_col"] = current_position[0]
            data["possible_moves"] = get_available_moves(data, current_position)
        return data
    else:
        return data


def assign_selected(data, row, col):
    active_row = data["active_row"]
    active_col = data["active_col"]
    start_string = convert_num_to_col(active_col) + str(active_row + 1)
    end_string = convert_num_to_col(col) + str(row + 1)
    if data["actively_jumping"]:
        data["move_string"] = data["move_string"] + f", "
    data["move_string"] = data["move_string"] + f"{start_string} to {end_string}"
    data["board"][row][col] = data["active_token"]
    data["board"][active_row][active_col] = 0
    return data


def select_token(data, row, col):
    data["active_token"] = data["board"][row][col]
    data["active_row"] = row
    data["active_col"] = col
    return data


def turn_reset(data):
    player_string = "Player " + str(data["active_player"])
    data["move_string"] = data["move_string"] + f" ({player_string})"
    data["move_list"].append(data["move_string"])
    data["move_string"] = ""
    data["active_player"] = 3 - data["active_player"]
    data["active_token"], data["active_row"], data["active_col"] = None, None, None
    data["jumped_list"] = []
    return data


def get_available_moves(data, pos_tuple):
    possible_moves = []
    possible_jumps = []
    jumpable = []
    p_row, p_col = pos_tuple[1], pos_tuple[0]
    if data["board"][p_row][p_col] != 0:
        position_dict = get_check_positions(pos_tuple)
        for index in range(0, 8):
            col = position_dict["adjacent"][index][0]
            row = position_dict["adjacent"][index][1]
            x_col = position_dict["extended"][index][0]
            x_row = position_dict["extended"][index][1]
            if (
                not is_outside((row, col))
                and data["board"][row][col] == 0
                and not data["actively_jumping"]
            ):
                possible_moves.append(position_dict["adjacent"][index])
            elif (
                not is_outside((x_col, x_row))
                and data["board"][x_row][x_col] == 0
                and (col, row) not in data["jumped_list"]
                and data["board"][row][col] != 0
            ):
                possible_jumps.append(position_dict["extended"][index])
                jumpable.append(position_dict["adjacent"][index])
    available_moves = {
        "possible_moves": possible_moves,
        "possible_jumps": possible_jumps,
        "jumpable": jumpable,
    }
    return available_moves


def get_check_positions(pos_tuple):
    row, col = pos_tuple[1], pos_tuple[0]
    position_dict = {
        "adjacent": [
            (col - 1, row - 1),  # top left
            (col, row - 1),  # above
            (col + 1, row - 1),  # top right
            (col - 1, row),  # left
            (col + 1, row),  # right
            (col - 1, row + 1),  # below left
            (col, row + 1),  # below
            (col + 1, row + 1),  # below right
        ],
        "extended": [
            (col - 2, row - 2),  # top left
            (col, row - 2),  # above
            (col + 2, row - 2),  # top right
            (col - 2, row),  # left
            (col + 2, row),  # right
            (col - 2, row + 2),  # below left
            (col, row + 2),  # below
            (col + 2, row + 2),  # below right
        ],
        "jumpable": [],
    }
    return position_dict


def is_outside(pos_tuple):
    board_size = 7
    return not 0 <= pos_tuple[0] < board_size or not 0 <= pos_tuple[1] < board_size


def get_jumped_position(move_col, move_row, col, row):
    if move_col == col:
        jumped_col = move_col
    elif move_col > col:
        jumped_col = move_col - 1
    else:
        jumped_col = move_col + 1
    if move_row == row:
        jumped_row = move_row
    elif move_row > row:
        jumped_row = move_row - 1
    else:
        jumped_row = move_row + 1
    jumped_position = (jumped_col, jumped_row)
    return jumped_position


def convert_num_to_col(num):
    return chr(ord("A") + num)
