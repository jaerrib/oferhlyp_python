from board import Board


class Game:

    def __init__(self):
        self.board = Board()
        self.move_list = {}
        self.jumped_list = []
        self.result = ""
        self.active_player = 1
        self.game_over = False
        self.turn_over = False

    @staticmethod
    def get_check_positions(pos_tuple):
        col, row = pos_tuple[0], pos_tuple[1]
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

    def is_outside(self, pos_tuple):
        board_size = len(self.board.data)
        return not 0 <= pos_tuple[0] < board_size or not 0 <= pos_tuple[1] < board_size

    def get_available_moves(self, pos_tuple):
        possible_moves = []
        possible_jumps = []
        jumpable = []
        if self.board.data[pos_tuple[1]][pos_tuple[0]] != 0:
            position_dict = self.get_check_positions(pos_tuple)
            for index in range(0, 8):
                col = position_dict["adjacent"][index][0]
                row = position_dict["adjacent"][index][1]
                x_col = position_dict["extended"][index][0]
                x_row = position_dict["extended"][index][1]
                if not self.is_outside((col, row)) and self.board.data[row][col] == 0:
                    possible_moves.append(position_dict["adjacent"][index])
                elif (
                    not self.is_outside((x_col, x_row))
                    and self.board.data[x_row][x_col] == 0
                    and self.board.data[x_row][x_col] not in self.jumped_list
                ):
                    possible_jumps.append(position_dict["extended"][index])
                    jumpable.append(position_dict["adjacent"][index])
        available_moves = {
            "possible_moves": possible_moves,
            "possible_jumps": possible_jumps,
            "jumpable": jumpable,
        }
        return available_moves

    def get_all_moves(self):
        for row in range(0, len(self.board.data)):
            for col in range(0, len(self.board.data[row])):
                pos_check = (col, row)
                my_moves = self.get_available_moves(pos_check)
                print(f"Moves for ({col}, {row}): {my_moves}")

    def change_player(self):
        self.active_player = 3 - self.active_player

    @staticmethod
    def convert_col_to_num(character):
        letters = "ABCDEFG"
        for index in range(0, len(letters)):
            if character.upper() == letters[index]:
                return index

    @staticmethod
    def convert_num_to_letter(num):
        return chr(ord("A") + num)

    def get_moves_list(self, move_list):
        converted_list = []
        for position in move_list["possible_moves"]:
            if position is not None:
                col = self.convert_num_to_letter(position[0])
                row = str(position[1] + 1)
                converted_list.append(col + row)
        for position in move_list["possible_jumps"]:
            if position is not None:
                col = self.convert_num_to_letter(position[0])
                row = str(position[1] + 1)
                converted_list.append(col + row)
        return converted_list

    def get_jumped_position(self, move_col, move_row, col, row):
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

    def reset_turn(self):
        self.jumped_list = []
        self.turn_over = False
        self.change_player()
        return self
