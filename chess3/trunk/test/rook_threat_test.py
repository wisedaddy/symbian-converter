__author__ = 'stafi'
import figures
import unittest


class RookThreatTest(unittest.TestCase):
    def test_p1(self):
        crds = {(0, 2),
                (1, 2),
                (2, 0),
                (2, 1),
                (2, 3),
                (3, 2)}
        self.assertSetEqual(crds, figures.rook_threat(2, 2, 4, 4))


if __name__ == '__main__':
    unittest.main()