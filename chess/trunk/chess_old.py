__author__ = "stafi"

import copy, strategy

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


def validate(brd, size_x, size_y):
    is_valid = 1
    for y in range(size_y):
        for x in range(size_x):
            fig = brd[y][x]
            if fig == king:
                is_valid = strategy.check_king_place_allowed(brd, x, y, size_x, size_y)
            elif fig == rook:
                is_valid = strategy.check_rook_place_allowed(brd, x, y, size_x, size_y)
            elif fig == bishop:
                is_valid = strategy.check_bishop_place_allowed(brd, x, y, size_x, size_y)
            elif fig == queen:
                is_valid = strategy.check_queen_place_allowed(brd, x, y, size_x, size_y)
            elif fig == knight:
                is_valid = strategy.check_knight_place_allowed(brd, x, y, size_x, size_y)
            if not is_valid: return 0
    return is_valid


def place_figs_on_brd(figs, brd, size_x, size_y, level):
    brds = set()
    fig = figs[0]
    #print('Level: ', level)
    other_figs = figs[1:]
    for y in range(size_y):
        for x in range(size_x):
            if brd[y][x] == 0:
                brd_copy = copy.deepcopy(brd)
                brd_copy[y][x] = fig
                if validate(brd_copy, size_x, size_y):
                    if (len(other_figs)) > 0:
                        other_brds = place_figs_on_brd(other_figs, brd_copy, size_x, size_y, level + 1)
                        for other_brd in other_brds:
                            brds.add(other_brd)
                    else:
                        brd_as_tuple = tuple(tuple(x) for x in brd_copy)
                        brds.add(brd_as_tuple)
    return brds
