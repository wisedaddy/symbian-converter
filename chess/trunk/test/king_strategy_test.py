__author__ = 'stafi'
import chess_old, strategy, unittest

class KingStrategyTest(unittest.TestCase):
    def test_king_strategy_positive1(self):
        size_x = 5
        size_y = 5
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][0] = "Q"
        self.assertTrue(strategy.check_king_place_allowed(brd, 2, 2, size_x, size_y))

    def test_king_strategy_negative1(self):
        size_x = 5
        size_y = 5
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[1][1] = "Q"
        self.assertFalse(strategy.check_king_place_allowed(brd, 2, 2, size_x, size_y))

if __name__ == '__main__':
    unittest.main()