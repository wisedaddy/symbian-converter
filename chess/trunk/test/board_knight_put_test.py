__author__ = 'stafi'
import chess, board, unittest

class BoardKnightPutTest(unittest.TestCase):

    def test_p1(self):
        size_x = 5
        size_y = 5
        brd = chess.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_knight(brd, 3, 2, size_x, size_y))
        chess.print_board(brd)
        self.assertTrue(brd[0][2] == board.threat)
        self.assertTrue(brd[0][4] == board.threat)
        self.assertTrue(brd[1][1] == board.threat)
        self.assertTrue(brd[3][1] == board.threat)
        self.assertTrue(brd[4][2] == board.threat)
        self.assertTrue(brd[4][4] == board.threat)
        self.assertTrue(brd[2][3] == board.knight)


    def test_p2(self):
        size_x = 5
        size_y = 5
        brd = chess.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_knight(brd, 2, 2, size_x, size_y))
        chess.print_board(brd)
        self.assertTrue(brd[0][1] == board.threat)
        self.assertTrue(brd[0][3] == board.threat)
        self.assertTrue(brd[1][0] == board.threat)
        self.assertTrue(brd[3][0] == board.threat)
        self.assertTrue(brd[4][1] == board.threat)
        self.assertTrue(brd[4][3] == board.threat)
        self.assertTrue(brd[2][2] == board.knight)


    def test_n1(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        board.put_bishop(brd, 0, 0, size_x, size_y)
        chess.print_board(brd)
        self.assertFalse(board.put_knight(brd, 2, 1, size_x, size_y))


if __name__ == '__main__':
    unittest.main()