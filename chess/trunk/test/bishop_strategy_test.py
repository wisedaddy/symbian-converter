__author__ = 'stafi'
import chess_old, strategy, unittest

class BishopStrategyTest(unittest.TestCase):

    def test_n1_check_bishop_place_allowed(self):
        size_x = 5
        size_y = 5
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][0] = "Q"
        self.assertFalse(strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y))

    def test_n2_check_bishop_place_allowed(self):
        size_x = 4
        size_y = 4
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][0] = "Q"
        self.assertFalse(strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y))

    def test_p1_check_bishop_place_allowed(self):
        size_x = 4
        size_y = 4
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][2] = "Q"
        self.assertTrue(strategy.check_bishop_place_allowed(brd, 2, 2, size_x, size_y))

    def test_p2_check_bishop_place_allowed(self):
        size_x = 3
        size_y = 3
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][0] = "Q"
        self.assertTrue(strategy.check_bishop_place_allowed(brd, 2, 1, size_x, size_y))

    def test_n3_check_bishop_place_allowed(self):
        size_x = 5
        size_y = 5
        brd = chess_old.create_empty_board(size_y, size_y)
        brd[0][2] = "Q"
        self.assertFalse(strategy.check_bishop_place_allowed(brd, 1, 3, size_x, size_y))

if __name__ == '__main__':
    unittest.main()