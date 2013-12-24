__author__ = 'stafi'
import figures
import unittest

class KingThreatTest(unittest.TestCase):

    def check_threat(self, crds, y, x):
        return (y, x) in crds

    def test_p1(self):
        size_x = 5
        size_y = 5
        crds = figures.king_threat(2, 2, size_y, size_x)
        self.assertTrue(self.check_threat(crds, 1, 1))
        self.assertTrue(self.check_threat(crds, 1, 2))
        self.assertTrue(self.check_threat(crds, 1, 3))
        self.assertTrue(self.check_threat(crds, 2, 1))
        self.assertTrue(self.check_threat(crds, 2, 3))
        self.assertTrue(self.check_threat(crds, 3, 1))
        self.assertTrue(self.check_threat(crds, 3, 2))
        self.assertTrue(self.check_threat(crds, 3, 3))


    def test_p2(self):
        size_x = 5
        size_y = 5
        crds = figures.king_threat(2, 0, size_y, size_x)
        self.assertTrue(self.check_threat(crds, 1, 0))
        self.assertTrue(self.check_threat(crds, 1, 1))
        self.assertTrue(self.check_threat(crds, 2, 1))
        self.assertTrue(self.check_threat(crds, 3, 0))
        self.assertTrue(self.check_threat(crds, 3, 1))


    def test_p3(self):
        size_x = 5
        size_y = 5
        crds = figures.king_threat(4, 4, size_y, size_x)
        self.assertTrue(self.check_threat(crds, 3, 4))
        self.assertTrue(self.check_threat(crds, 3, 3))
        self.assertTrue(self.check_threat(crds, 4, 3))


if __name__ == '__main__':
    unittest.main()