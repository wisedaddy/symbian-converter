__author__ = 'stafi'
import chess2, board, unittest, view


class BoardBishopMarkTest(unittest.TestCase):
    def test_p3(self):
        size_x = 3
        size_y = 3
        brd = chess2.create_empty_board(size_y, size_y)
        self.assertTrue(board.check_and_mark_bishop_threat(brd, 1, 1, size_x, size_y))
        view.print_board(brd)
        self.assertTrue(brd[0][0] == "X")
        self.assertTrue(brd[0][2] == "X")
        self.assertTrue(brd[2][0] == "X")
        self.assertTrue(brd[2][2] == "X")

    def test_p1(self):
        size_x = 4
        size_y = 4
        brd = chess2.create_empty_board(size_y, size_y)
        self.assertTrue(board.check_and_mark_bishop_threat(brd, 2, 1, size_x, size_y))
        view.print_board(brd)
        self.assertTrue(brd[0][1] == "X")
        self.assertTrue(brd[0][3] == "X")
        self.assertTrue(brd[2][1] == "X")
        self.assertTrue(brd[2][3] == "X")

if __name__ == '__main__':
    unittest.main()