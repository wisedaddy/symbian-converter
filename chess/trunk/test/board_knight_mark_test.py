__author__ = 'stafi'
import chess2, board, view, unittest

class BoardKnightMarkTest(unittest.TestCase):

    def test_p1(self):
        size_x = 5
        size_y = 5
        brd = chess2.create_empty_board(size_y, size_y)
        board.put_knight(brd, 3, 2, size_x, size_y)
        view.print_board(brd)

if __name__ == '__main__':
    unittest.main()