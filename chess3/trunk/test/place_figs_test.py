__author__ = 'stafi'
import board
import figures
import unittest


class PlaceFigsTest(unittest.TestCase):
    def internal_figs_test(self, figs, size_y, size_x):
        return board.place_figs(figs, size_y, size_x)

    def test_queen_p1(self):
        size_x = 2
        size_y = 2
        figs = figures.QUEEN,
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)

    def test_queen_p2(self):
        size_x = 4
        size_y = 4
        figs = figures.QUEEN,
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 16)

    def test_queen_p3(self):
        size_x = 2
        size_y = 2
        figs = figures.QUEEN, figures.QUEEN,
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 0)

    def test_knight_p1(self):
        size_x = 2
        size_y = 2
        figs = figures.KNIGHT, figures.KNIGHT
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 6)

    def test_2kings1rook(self):
        size_x = 3
        size_y = 3
        figs = figures.KING, figures.KING, figures.ROOK
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)

    def test_1(self):
        size_x = 2
        size_y = 2
        figs = figures.ROOK, figures.KNIGHT
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)

    def test_2rooks_4knights(self):
        size_x = 4
        size_y = 4
        figs_map = {
            figures.KING: 0,
            figures.QUEEN: 0,
            figures.BISHOP: 0,
            figures.ROOK: 2,
            figures.KNIGHT: 4
        }
        figs = figures.figs_as_list(figs_map)
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 8)

    def test_2kings(self):
        size_x = 3
        size_y = 2
        figs_map = {
            figures.KING: 2,
            figures.QUEEN: 0,
            figures.BISHOP: 0,
            figures.ROOK: 0,
            figures.KNIGHT: 0
        }
        figs = figures.figs_as_list(figs_map)
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)

    def test_5knights(self):
        size_x = 3
        size_y = 3
        figs_map = {
            figures.KING: 0,
            figures.QUEEN: 0,
            figures.BISHOP: 0,
            figures.ROOK: 0,
            figures.KNIGHT: 5
        }
        figs = figures.figs_as_list(figs_map)
        brds = self.internal_figs_test(figs, size_y, size_x)
        #for brd in brds:
        #    board.print_board(board.unpack(brd, size_x, size_y))
        self.assertEqual(len(brds), 2)


if __name__ == '__main__':
    unittest.main()