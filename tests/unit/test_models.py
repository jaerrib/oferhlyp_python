import unittest

from board import Board
from game import Game


class TestGame(unittest.TestCase):

    def test_new_game(self):
        game = Game()
        self.assertEqual(game.move_list, {})
        self.assertEqual(game.result, "")
        self.assertEqual(game.active_player, 1)


if __name__ == "__main__":
    unittest.main()
