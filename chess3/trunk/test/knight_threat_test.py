__author__ = 'stafi'
import figures
import unittest


class KnightThreatTest(unittest.TestCase):
    def test_p1(self):
        crds = {(2, 0),
                (4, 0),
                (1, 1),
                (1, 3),
                (2, 4),
                (4, 4)}
        self.assertSetEqual(crds, figures.knight_threat(3, 2, 5, 5))

    def test_p2(self):
        crds = {(1, 0),
                (3, 0),
                (0, 1),
                (0, 3),
                (1, 4),
                (3, 4),
                (4, 1),
                (4, 3)}
        self.assertSetEqual(crds, figures.knight_threat(2, 2, 5, 5))


if __name__ == '__main__':
    unittest.main()