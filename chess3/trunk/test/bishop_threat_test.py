__author__ = 'stafi'
import figures
import unittest


class BishopThreatTest(unittest.TestCase):
    def test_p1(self):
        crds = {(0, 0),
                (0, 2),
                (2, 0),
                (2, 2)}
        self.assertSetEqual(crds, figures.bishop_threat(1, 1, 3, 3))

    def test_p2(self):
        crds = {(0, 1),
                (0, 3),
                (2, 1),
                (2, 3),
                (3, 0)}
        self.assertSetEqual(crds, figures.bishop_threat(1, 2, 4, 4))


    def test_p3(self):
        crds = {(3, 1),
                (2, 0),
                (3, 3),
                (2, 4)}
        self.assertSetEqual(crds, figures.bishop_threat(4, 2, 5, 5))


if __name__ == '__main__':
    unittest.main()