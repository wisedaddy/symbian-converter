__author__ = "stafi"

import board, view
import copy

king = b"K"
queen = b"Q"
bishop = b"B"
knight = b"N"
rook = b"R"
empty = b"0"
threat = b"T"


def figs_as_list(figs):
    fig_list = []
    for k, v in figs.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


def create_empty_board(x, y):
    return [[empty for xindex in range(x)] for yindex in range(y)]


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
            if brd_copy[y][x] == empty:
                brd_copy[y][x] = threat
    return brd_copy


def pack_board(brd, size_x, size_y):
    packed = ()
    for y in range(size_y):
        for x in range(size_x):
            if not board.free_of_figures(brd, y, x):
                packed += y, x, brd[y][x]
    return packed


def unpack_board(packed, size_x, size_y):
    brd = create_empty_board(size_x, size_y)
    for i in range(len(packed)//3):
        y = packed[i*3]
        x = packed[i*3+1]
        f = packed[i*3+2]
        brd[y][x] = f
    return brd


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
                        stored_board = pack_board(brd_copy, size_x, size_y)
                        brds.add(stored_board)
                        # view.print_board(stored_board)
    return brds
