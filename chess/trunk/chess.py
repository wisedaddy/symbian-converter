__author__ = "stafi"

import board

view_figures = {
    board.king: "K",
    board.queen: "Q",
    board.bishop: "B",
    board.knight: "N",
    board.rook: "R",
    board.empty: "0",
    board.threat: "T"
}

# Prints board contents to console
def print_board(brd):
    if len(brd) > 0:
        for row in brd: print("|".join([view_figures[f] for f in row]))
        print("--" * (len(brd[0])))


# Returns map of (figures: counts) as list
def figs_as_list(figs):
    fig_list = []
    for k, v in figs.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


# Create an empty board (list of lists)
def create_empty_board(x, y):
    return [[board.empty for xindex in range(x)] for yindex in range(y)]


# Compacts board presentation (list of lists) for storing in set
# The board is stored as tuple, which consists of coordinates followed by figure type:
#   y1, x1, figure1, y2, x2, figure2, ..., yN, xN, figureN
def pack_board(brd, size_x, size_y):
    packed = ()
    for y in range(size_y):
        for x in range(size_x):
            if not board.free_of_figures(brd, y, x):
                packed += y, x, brd[y][x]
    return packed


# Unpacks board from compact presentation and return list of lists
# See pack_board for information on compact board presentation
def unpack_board(packed, size_x, size_y):
    brd = create_empty_board(size_x, size_y)
    for i in range(len(packed)//3):
        y = packed[i*3]
        x = packed[i*3+1]
        f = packed[i*3+2]
        brd[y][x] = f
    return brd


# Function tries to put list of figures on board and returns the set of distinct packed boards where all figures are put on board
# The function call itself recursively to try all the figures
def place_figs_on_brd(figs, brd, size_x, size_y):
    brds = set()
    if len(figs) > 0:
        fig = figs[0]
        other_figs = figs[1:]
        for y in range(size_y):
            for x in range(size_x):
                if board.free_of_threat(brd, y, x):
                    brd_copy = [row[:] for row in brd]
                    if board.func_put_fig[fig](brd_copy, x, y, size_x, size_y):
                        if (len(other_figs)) > 0:
                            other_brds = place_figs_on_brd(other_figs, brd_copy, size_x, size_y)
                            if len(other_brds) > 0:
                                brds |= other_brds
                        else:
                            packed_board = pack_board(brd_copy, size_x, size_y)
                            brds.add(packed_board)
    return brds
