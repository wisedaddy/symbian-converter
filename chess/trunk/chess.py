__author__ = "stafi"

import board

def figs_as_list(figs):
    fig_list = []
    for k, v in figs.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


def create_empty_board(x, y):
    return [[board.empty for xindex in range(x)] for yindex in range(y)]

def pack_board(brd, size_x, size_y):
    packed = ()
    for y in range(size_y):
        for x in range(size_x):
            if not board.free_of_figures(brd, y, x):
                packed = packed + ((y, x, brd[y][x]),)
    return packed


def unpack_board(packed, size_x, size_y):
    brd = create_empty_board(size_x, size_y)
    for entry in packed:
        y, x, f = entry
        brd[y][x] = f
    return brd


def place_figs_on_brd(figs, brd, size_x, size_y):
    brds = set()
    fig = figs[0]
    other_figs = figs[1:]
    for y in range(size_y):
        for x in range(size_x):
            if board.free_of_threat(brd, y, x):
                brd_copy = [row[:] for row in brd]
                if board.func_put_fig[fig](brd_copy, x, y, size_x, size_y):
                    if (len(other_figs)) > 0:
                        other_brds = place_figs_on_brd(other_figs, brd_copy, size_x, size_y)
                        brds = brds | other_brds
                    else:
                        stored_board = pack_board(brd_copy, size_x, size_y)
                        brds.add(stored_board)
    return brds
