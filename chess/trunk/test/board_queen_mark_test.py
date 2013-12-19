__author__ = 'stafi'
import chess2, board, unittest, view

class BoardQueenMarkTest(unittest.TestCase):
    def test_p1(self):
        size_x = 4
        size_y = 4
        brd = chess2.create_empty_board(size_y, size_y)
        self.assertTrue(board.put_queen(brd, 0, 0, size_x, size_y))
        view.print_board(brd)

if __name__ == '__main__':
    unittest.main()