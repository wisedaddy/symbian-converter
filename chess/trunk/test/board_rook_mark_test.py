__author__ = 'stafi'
import chess, board, unittest, view


class BoardRookMarkTest(unittest.TestCase):

    def test_p1(self):
        size_x = 4
        size_y = 4
        brd = chess.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_rook(brd, 2, 2, size_x, size_y))
        self.assertFalse(board.put_bishop(brd, 1, 1, size_x, size_y))

if __name__ == '__main__':
    unittest.main()