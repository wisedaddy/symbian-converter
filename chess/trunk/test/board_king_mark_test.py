__author__ = 'stafi'
import chess, board, view, unittest

class KingStrategyTest(unittest.TestCase):
    def test_n1(self):
        size_x = 5
        size_y = 5
        brd = chess.create_empty_board(size_y, size_y)
        board.put_queen(brd, 0, 0, size_x, size_y)
        self.assertFalse(board.put_king(brd, 2, 2, size_x, size_y))
        view.print_board(brd)

    def test_n2(self):
        size_x = 5
        size_y = 5
        brd = chess.create_empty_board(size_y, size_y)
        board.put_queen(brd, 1, 1, size_x, size_y)
        self.assertFalse(board.put_king(brd, 2, 2, size_x, size_y))
        view.print_board(brd)

    def test_p1(self):
        size_x = 5
        size_y = 5
        brd = chess.create_empty_board(size_y, size_y)
        board.put_queen(brd, 0, 1, size_x, size_y)
        self.assertTrue(board.put_king(brd, 2, 2, size_x, size_y))
        view.print_board(brd)

if __name__ == '__main__':
    unittest.main()