__author__ = 'stafi'

import datetime
import chess, view

size_x = 6
size_y = 9
figs = {
    chess.king: 2,
    chess.queen: 1,
    chess.bishop: 1,
    chess.rook: 1,
    chess.knight: 1
}


def main():
    time1 = datetime.datetime.now()
    fig_list = chess.figs_as_list(figs)
    root_brd = chess.create_empty_board(size_x, size_y)
    brds = chess.place_figs_on_brd(fig_list, root_brd, size_x, size_y, 0)
    for brd in brds:
        view.print_board(brd)
    print("Number of boards: ", len(brds))
    print("Time: ", datetime.datetime.now() - time1)

main()