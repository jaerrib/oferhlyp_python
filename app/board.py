from os import system

from app.game_pieces import King, Man


class Board:

    def __init__(self) -> None:
        self.data: list = []
        self.create()
        self.setup()

    def create(self):
        size: int = 7
        empty: int = 0
        for row_num in range(size):
            row: list = []
            for col_num in range(size):
                row.append(empty)
            self.data.append(row)
        return self

    def setup(self):
        for row in range(0, 2):
            for col in range(0, 7):
                self.data[row][col]: Man = Man(2).__dict__
        self.data[0][3]: King = King(2).__dict__
        for row in range(5, 7):
            for col in range(0, 7):
                self.data[row][col]: Man = Man(1).__dict__
        self.data[6][3]: King = King(1).__dict__
        return self

    def display_board(self) -> None:
        system("clear")
        print("    A  B  C  D  E  F  G")
        for row in range(0, 7):
            print(f"{row + 1} |", end="")
            for col in range(0, 7):
                if self.data[row][col] == 0:
                    print("__|", end="")
                else:
                    class_type = type(self.data[row][col]).__name__[:1]
                    if self.data[row][col]["hp"] == 1:
                        class_type = class_type.lower()
                    player: int = self.data[row][col]["player"]
                    print(f"{class_type}{player}|", end="")
            print("")
        print("")
