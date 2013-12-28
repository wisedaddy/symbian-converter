__author__ = 'stafi'
import figures
import unittest


class KingThreatTest(unittest.TestCase):
    def test_p1(self):
        crds = {(1, 1),
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 3),
                (3, 1),
                (3, 2),
                (3, 3)}
        self.assertSetEqual(crds, figures.king_threat(2, 2, 5, 5))

    def test_p2(self):
        crds = {(1, 0),
                (1, 1),
                (2, 1),
                (3, 0),
                (3, 1)}
        self.assertSetEqual(crds, figures.king_threat(2, 0, 5, 5))

    def test_p3(self):
        crds = {(3, 4),
                (3, 3),
                (4, 3)}
        self.assertSetEqual(crds, figures.king_threat(4, 4, 5, 5))


if __name__ == '__main__':
    unittest.main()