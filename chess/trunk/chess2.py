__author__ = "stafi"

import board, view
import copy

king = "K"
queen = "Q"
bishop = "B"
knight = "N"
rook = "R"


def figs_as_list(figs):
    fig_list = []
    for k, v in figs.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


def create_empty_board(x, y):
    return [[0 for xindex in range(x)] for yindex in range(y)]


def place_fig_on_board(fig, brd, x, y, size_x, size_y):
    if fig == king:
        res = board.put_king(brd, x, y, size_x, size_y)
    elif fig == rook:
        res = board.put_rook(brd, x, y, size_x, size_y)
    elif fig == bishop:
        res = board.put_bishop(brd, x, y, size_x, size_y)
    elif fig == queen:
        res = board.put_queen(brd, x, y, size_x, size_y)
    elif fig == knight:
        res = board.put_knight(brd, x, y, size_x, size_y)
    return res


def replaceZeros(brd_copy):
    for y in range(len(brd_copy)):
        for x in range(len(brd_copy[y])):
            if brd_copy[y][x] == 0:
                brd_copy[y][x] = "X"
    return brd_copy


def place_figs_on_brd(figs, brd, size_x, size_y):
    brds = set()
    fig = figs[0]
    #print('Level: ', level)
    other_figs = figs[1:]
    for y in range(size_y):
        for x in range(size_x):
            if board.free_of_threat(brd, y, x):
                brd_copy = copy.deepcopy(brd)
                if place_fig_on_board(fig, brd_copy, x, y, size_x, size_y):
                    if (len(other_figs)) > 0:
                        other_brds = place_figs_on_brd(other_figs, brd_copy, size_x, size_y)
                        for other_brd in other_brds:
                            brds.add(other_brd)
                    else:
                        replaceZeros(brd_copy)
                        brd_as_tuple = tuple(tuple(f) for f in brd_copy)
                        brds.add(brd_as_tuple)
                        #view.print_board(brd_copy)
    return brds
