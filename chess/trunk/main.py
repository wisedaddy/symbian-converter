__author__ = 'stafi'

import datetime, sys
import chess, board

size_x = 6
size_y = 9
figs = {
    board.king: 2,
    board.queen: 1,
    board.bishop: 1,
    board.rook: 1,
    board.knight: 1
}


def print_board(brd):
    for row in brd: print("|".join(row))
    print("--" * (len(brd)))


def main():
    time1 = datetime.datetime.now()
    print("Start time: ", time1)
    fig_list = chess.figs_as_list(figs)
    root_brd = chess.create_empty_board(size_x, size_y)
    brds = chess.place_figs_on_brd(fig_list, root_brd, size_x, size_y)
    time2 = datetime.datetime.now()
    for brd in brds: print_board(chess.unpack_board(brd, size_x, size_y))
    print("Boards storage size (b): ", sys.getsizeof(brds))
    print("Number of boards: ", len(brds))
    print("Execution time: ", time2 - time1)

main()
