from game_pieces import Man, King
from os import system


class Board:

    def __init__(self):
        self.data = []
        self.create()
        self.setup()

    def create(self):
        size = 7
        empty = 0
        for row_num in range(size):
            row = []
            for col_num in range(size):
                row.append(empty)
            self.data.append(row)
        return self

    def setup(self):
        for row in range(0, 2):
            for col in range(0, 7):
                self.data[row][col] = Man(2)
        self.data[0][3] = King(2)
        for row in range(5, 7):
            for col in range(0, 7):
                self.data[row][col] = Man(1)
        self.data[6][3] = King(1)
        return self

    def display_board(self):
        system('clear')
        print("    A  B  C  D  E  F  G")
        for row in range(0, 7):
            print(f"{row + 1} |", end="")
            for col in range(0, 7):
                if self.data[row][col] == 0:
                    print("__|", end="")
                else:
                    class_type = type(self.data[row][col]).__name__[:1]
                    if self.data[row][col].hp == 1:
                        class_type = class_type.lower()
                    player = self.data[row][col].player
                    print(f"{class_type}{player}|", end="")
            print("")
        print("")
