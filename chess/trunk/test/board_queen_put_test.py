__author__ = 'stafi'
import chess, board, unittest

class BoardQueenMarkTest(unittest.TestCase):
    def test_p1(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_queen(brd, 0, 0, size_x, size_y))
        chess.print_board(brd)
        self.assertTrue(brd[0][1] == board.threat)
        self.assertTrue(brd[0][2] == board.threat)
        self.assertTrue(brd[0][3] == board.threat)
        self.assertTrue(brd[1][0] == board.threat)
        self.assertTrue(brd[2][0] == board.threat)
        self.assertTrue(brd[3][0] == board.threat)
        self.assertTrue(brd[1][1] == board.threat)
        self.assertTrue(brd[0][0] == board.queen)


    def test_p2(self):
        size_x = 5
        size_y = 5
        brd = chess.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_queen(brd, 2, 2, size_x, size_y))
        chess.print_board(brd)
        self.assertTrue(brd[1][1] == board.threat)
        self.assertTrue(brd[1][2] == board.threat)
        self.assertTrue(brd[1][3] == board.threat)
        self.assertTrue(brd[2][1] == board.threat)
        self.assertTrue(brd[2][3] == board.threat)
        self.assertTrue(brd[3][1] == board.threat)
        self.assertTrue(brd[3][2] == board.threat)
        self.assertTrue(brd[3][3] == board.threat)
        self.assertTrue(brd[0][0] == board.threat)
        self.assertTrue(brd[0][2] == board.threat)
        self.assertTrue(brd[0][4] == board.threat)
        self.assertTrue(brd[4][0] == board.threat)
        self.assertTrue(brd[4][2] == board.threat)
        self.assertTrue(brd[4][4] == board.threat)
        self.assertTrue(brd[2][0] == board.threat)
        self.assertTrue(brd[2][4] == board.threat)
        self.assertTrue(brd[0][1] == board.empty)
        self.assertTrue(brd[0][3] == board.empty)
        self.assertTrue(brd[4][1] == board.empty)
        self.assertTrue(brd[4][3] == board.empty)


    def test_n1(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        board.put_bishop(brd, 0, 0, size_x, size_y)
        chess.print_board(brd)
        self.assertFalse(board.put_queen(brd, 3, 0, size_x, size_y))


    def test_n2(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        board.put_rook(brd, 1, 2, size_x, size_y)
        chess.print_board(brd)
        self.assertFalse(board.put_queen(brd, 0, 1, size_x, size_y))


if __name__ == '__main__':
    unittest.main()