import unittest

from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_new_game(self):
        self.assertEqual(self.game.move_list, {})
        self.assertEqual(self.game.result, "")
        self.assertEqual(self.game.active_player, 1)

    def test_get_check_positions(self):
        self.assertEqual(
            self.game.get_check_positions((4, 4)),
            {
                "adjacent": [
                    (3, 3),
                    (4, 3),
                    (5, 3),
                    (3, 4),
                    (5, 4),
                    (3, 5),
                    (4, 5),
                    (5, 5),
                ],
                "extended": [
                    (2, 2),
                    (4, 2),
                    (6, 2),
                    (2, 4),
                    (6, 4),
                    (2, 6),
                    (4, 6),
                    (6, 6),
                ],
                "jumpable": [],
            },
        )

    def test_is_outside(self):
        self.assertEqual(self.game.is_outside((10, 10)), True)
        self.assertEqual(self.game.is_outside((4, 4)), False)

    def test_get_available_moves(self):
        self.assertEqual(
            self.game.get_available_moves((0, 0)),
            {
                "possible_moves": [],
                "possible_jumps": [(0, 2), (2, 2)],
                "jumpable": [(0, 1), (1, 1)],
            },
        )
        self.assertEqual(
            self.game.get_available_moves((3, 6)),
            {
                "possible_moves": [],
                "possible_jumps": [(1, 4), (3, 4), (5, 4)],
                "jumpable": [(2, 5), (3, 5), (4, 5)],
            },
        )
        self.assertEqual(
            self.game.get_available_moves((3, 5)),
            {
                "possible_moves": [(2, 4), (3, 4), (4, 4)],
                "possible_jumps": [],
                "jumpable": [],
            },
        )


if __name__ == "__main__":
    unittest.main()
