__author__ = 'stafi'
import chess3, figures, unittest


class PlaceFigsTest(unittest.TestCase):

    def internal_figs_test(self, figs, size_y, size_x):
        brds = set()
        chess3.place_figs(figs, brds, size_y, size_x)
        return brds

    
    def test_queen_p1(self):
        size_x = 2
        size_y = 2
        figs = figures.queen,
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)
    
    
    def test_queen_p2(self):
        size_x = 4
        size_y = 4
        figs = figures.queen,
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 16)
    
    
    def test_queen_p3(self):
        size_x = 2
        size_y = 2
        figs = figures.queen, figures.queen,
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 0)
    
    
    def test_knight_p1(self):
        size_x = 2
        size_y = 2
        figs = figures.knight, figures.knight
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 6)


    def test_2kings1rook(self):
        size_x = 3
        size_y = 3
        figs = figures.king, figures.king, figures.rook
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)


    def test_1(self):
        size_x = 2
        size_y = 2
        figs = figures.rook, figures.knight
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)


    def test_2rooks_4knights(self):
        size_x = 4
        size_y = 4
        figs_map = {
            figures.king: 0,
            figures.queen: 0,
            figures.bishop: 0,
            figures.rook: 2,
            figures.knight: 4
        }
        figs = chess3.figs_as_list(figs_map)
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 8)


    def test_2kings(self):
        size_x = 3
        size_y = 2
        figs_map = {
            figures.king: 2,
            figures.queen: 0,
            figures.bishop: 0,
            figures.rook: 0,
            figures.knight: 0
        }
        figs = chess3.figs_as_list(figs_map)
        brds = self.internal_figs_test(figs, size_y, size_x)
        self.assertEqual(len(brds), 4)


    def test_5knights(self):
        size_x = 3
        size_y = 3
        figs_map = {
            figures.king: 0,
            figures.queen: 0,
            figures.bishop: 0,
            figures.rook: 0,
            figures.knight: 5
        }
        figs = chess3.figs_as_list(figs_map)
        brds = self.internal_figs_test(figs, size_y, size_x)
        #for brd in brds:
        #     chess3.print_board(chess3.unpack(brd, size_x, size_y))
        self.assertEqual(len(brds), 2)


if __name__ == '__main__':
    unittest.main()