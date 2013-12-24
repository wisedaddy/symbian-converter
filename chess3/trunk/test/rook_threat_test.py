__author__ = 'stafi'
import figures, unittest


class RookThreatTest(unittest.TestCase):


    def check_threat(self, crds, y, x):
        return (y, x) in crds


    def test_p1(self):
        size_x = 4
        size_y = 4
        brd = figures.rook_threat(2, 2, size_y, size_x)
        self.assertTrue(self.check_threat(brd, 0, 2))
        self.assertTrue(self.check_threat(brd, 1, 2))
        self.assertTrue(self.check_threat(brd, 2, 0))
        self.assertTrue(self.check_threat(brd, 2, 1))
        self.assertTrue(self.check_threat(brd, 2, 3))
        self.assertTrue(self.check_threat(brd, 3, 2))


if __name__ == '__main__':
    unittest.main()