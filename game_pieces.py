class Man:

    def __init__(self, player):
        self.hp = 2
        self.player = player
        self.is_king = False


class King:

    def __init__(self, player):
        self.hp = 2
        self.player = player
        self.is_king = True
