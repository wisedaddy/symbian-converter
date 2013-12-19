__author__ = 'stafi'
import chess_old, strategy, unittest

class QueenStrategyTest(unittest.TestCase):

    def test_n1_check_bishop_place_allowed(self):
        size_x = 5
        size_y = 5
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][2] = "Q"
        self.assertFalse(strategy.check_queen_place_allowed(brd, 2, 2, size_x, size_y))

    def test_n2_check_bishop_place_allowed(self):
        size_x = 4
        size_y = 4
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[2][3] = "Q"
        self.assertFalse(strategy.check_queen_place_allowed(brd, 2, 2, size_x, size_y))

    def test_p1_check_bishop_place_allowed(self):
        size_x = 4
        size_y = 4
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][2] = "Q"
        self.assertTrue(strategy.check_queen_place_allowed(brd, 0, 1, size_x, size_y))

    def test_n3_check_bishop_place_allowed(self):
        size_x = 5
        size_y = 5
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][2] = "Q"
        self.assertFalse(strategy.check_queen_place_allowed(brd, 3, 1, size_x, size_y))

if __name__ == '__main__':
    unittest.main()