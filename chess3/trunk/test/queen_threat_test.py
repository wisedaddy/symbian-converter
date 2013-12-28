__author__ = 'stafi'
import figures
import unittest


class QueenThreatTest(unittest.TestCase):
    def test_p1(self):
        crds = {(0, 1),
                (0, 2),
                (0, 3),
                (1, 0),
                (2, 0),
                (3, 0),
                (1, 1),
                (2, 2),
                (3, 3)}
        self.assertSetEqual(crds, figures.queen_threat(0, 0, 4, 4))

    def test_p2(self):
        size_x = 5
        size_y = 5
        crds = {(1, 1),
                (1, 2),
                (1, 3),
                (2, 1),
                (2, 3),
                (3, 1),
                (3, 2),
                (3, 3),
                (0, 0),
                (0, 2),
                (0, 4),
                (4, 0),
                (4, 2),
                (4, 4),
                (2, 0),
                (2, 4)}
        self.assertEqual(crds, figures.queen_threat(2, 2, size_y, size_x))


if __name__ == '__main__':
    unittest.main()