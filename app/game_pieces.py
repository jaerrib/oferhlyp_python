class Man:

    def __init__(self, player: int):
        self.hp: int = 2
        self.player: int = player
        self.is_king: bool = False


class King:

    def __init__(self, player: int):
        self.hp: int = 2
        self.player: int = player
        self.is_king: bool = True
