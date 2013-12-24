__author__ = 'stafi'
import chess, board, unittest


class BoardRookPutTest(unittest.TestCase):


    def test_p1(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_rook(brd, 2, 2, size_x, size_y))
        chess.print_board(brd)
        self.assertTrue(brd[0][2] == board.threat)
        self.assertTrue(brd[1][2] == board.threat)
        self.assertTrue(brd[2][0] == board.threat)
        self.assertTrue(brd[2][1] == board.threat)
        self.assertTrue(brd[2][3] == board.threat)
        self.assertTrue(brd[3][2] == board.threat)
        self.assertTrue(brd[2][2] == board.rook)


    def test_n1(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        board.put_bishop(brd, 0, 0, size_x, size_y)
        chess.print_board(brd)
        self.assertFalse(board.put_rook(brd, 3, 0, size_x, size_y))


if __name__ == '__main__':
    unittest.main()