__author__ = 'stafi'
import figures
import unittest

class BishopThreatTest(unittest.TestCase):

    def check_threat(self, crds, y, x):
        return (y, x) in crds


    def test_p1(self):
        size_x = 3
        size_y = 3
        brd = figures.bishop_threat(1, 1, size_y, size_x)
        self.assertTrue(self.check_threat(brd, 0, 0))
        self.assertTrue(self.check_threat(brd, 0, 2))
        self.assertTrue(self.check_threat(brd, 2, 0))
        self.assertTrue(self.check_threat(brd, 2, 2))


    def test_p2(self):
        size_x = 4
        size_y = 4
        brd = figures.bishop_threat(1, 2, size_y, size_x)
        self.assertTrue(self.check_threat(brd, 0, 1))
        self.assertTrue(self.check_threat(brd, 0, 3))
        self.assertTrue(self.check_threat(brd, 2, 1))
        self.assertTrue(self.check_threat(brd, 2, 3))


    def test_p3(self):
        size_x = 5
        size_y = 5
        brd = figures.bishop_threat(4, 2, size_y, size_x)
        self.assertTrue(self.check_threat(brd, 3, 1))
        self.assertTrue(self.check_threat(brd, 2, 0))
        self.assertTrue(self.check_threat(brd, 3, 3))
        self.assertTrue(self.check_threat(brd, 2, 4))


if __name__ == '__main__':
    unittest.main()