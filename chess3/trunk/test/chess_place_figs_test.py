__author__ = 'stafi'
import chess3, figures, unittest


class ChessPlaceFigsTest(unittest.TestCase):

    def test_queen_p1(self):
        size_x = 2
        size_y = 2
        figs = board.queen,
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 4)


    def test_queen_p2(self):
        size_x = 4
        size_y = 4
        figs = board.queen,
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 16)


    def test_queen_p3(self):
        size_x = 2
        size_y = 2
        figs = board.queen, board.queen,
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 0)


    def test_knight_p1(self):
        size_x = 2
        size_y = 2
        figs = board.knight, board.knight
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 6)


    def test_2kings1rook(self):
        size_x = 3
        size_y = 3
        figs = board.king, board.king, board.rook
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 4)


    def test_2rooks_4knights(self):
        size_x = 4
        size_y = 4
        figs_map = {
            board.king: 0,
            board.queen: 0,
            board.bishop: 0,
            board.rook: 2,
            board.knight: 4
        }
        figs = chess.figs_as_list(figs_map)
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 8)


    def test_2kings(self):
        size_x = 3
        size_y = 2
        figs_map = {
            board.king: 2,
            board.queen: 0,
            board.bishop: 0,
            board.rook: 0,
            board.knight: 0
        }
        figs = chess.figs_as_list(figs_map)
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_x, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 4)


    def test_5knights(self):
        size_x = 3
        size_y = 3
        figs_map = {
            board.king: 0,
            board.queen: 0,
            board.bishop: 0,
            board.rook: 0,
            board.knight: 5
        }
        figs = chess.figs_as_list(figs_map)
        brds = chess.place_figs_on_brd(figs, chess.create_empty_board(size_y, size_y),
                                size_x, size_y)
        self.assertEqual(len(brds), 2)


if __name__ == '__main__':
    unittest.main()