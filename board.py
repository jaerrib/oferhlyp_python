from game_pieces import Man, King


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
                self.data[row][col] = Man(1)
        self.data[0][3] = King(1)
        for row in range(5, 7):
            for col in range(0, 7):
                self.data[row][col] = Man(1)
        self.data[6][3] = King(1)
        return self
