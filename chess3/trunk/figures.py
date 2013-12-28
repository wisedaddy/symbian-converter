__author__ = 'stafi'

KING = 1
QUEEN = 2
BISHOP = 3
KNIGHT = 4
ROOK = 5
EMPTY = 0


# Returns map of (figures: counts) as list
def figs_as_list(figs_dict):
    fig_list = []
    for k, v in figs_dict.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


# Returns a set of coordinates of board spots which are threatened by a KING place at (y, x)
def king_threat(y, x, size_y, size_x):
    crds = set()
    if y > 0:
        crds.add((y - 1, x))
    if y < size_y - 1:
        crds.add((y + 1, x))
    if x > 0:
        crds.add((y, x - 1))
        if y > 0:
            crds.add((y - 1, x - 1))
        if y < size_y - 1:
            crds.add((y + 1, x - 1))
    if x < size_x - 1:
        crds.add((y, x + 1))
        if y > 0:
            crds.add((y - 1, x + 1))
        if y < size_y - 1:
            crds.add((y + 1, x + 1))
    return crds


# Returns a set of coordinates of board spots which are threatened by a ROOK place at (y, x)
def rook_threat(y, x, size_y, size_x):
    crds = set()
    for col in range(size_x):
        if col != x:
            crds.add((y, col))
    for row in range(size_y):
        if row != y:
            crds.add((row, x))
    return crds


# Returns a set of coordinates of board spots which are threatened by a BISHOP place at (y, x)
def bishop_threat(y, x, size_y, size_x):
    crds = set()
    min_x_y = min(x, y)
    x1 = x - min_x_y
    y1 = y - min_x_y
    i = 0
    while y1 + i < size_y and x1 + i < size_x:
        if x1 + i != x and y1 + i != y:
            crds.add((y1 + i, x1 + i))
        i += 1
    min_x_y = min(x, size_y - y - 1)
    x1 = x - min_x_y
    y1 = y + min_x_y
    i = 0
    while y1 - i >= 0 and x1 + i < size_x:
        if x1 + i != x and y1 - i != y:
            crds.add((y1 - i, x1 + i))
        i += 1
    return crds


# Returns a set of coordinates of board spots which are threatened by a QUEEN place at (y, x)
def queen_threat(y, x, size_y, size_x):
    return rook_threat(y, x, size_y, size_x) | bishop_threat(y, x, size_y, size_x)


# Returns a set of coordinates of board spots which are threatened by a KNIGHT place at (y, x)
def knight_threat(y, x, size_y, size_x):
    crds = set()
    if x > 0 and y > 1:
        crds.add((y - 2, x - 1))
    if x > 1 and y > 0:
        crds.add((y - 1, x - 2))
    if x < size_x - 1 and y > 1:
        crds.add((y - 2, x + 1))
    if x < size_x - 2 and y > 0:
        crds.add((y - 1, x + 2))
    if x > 0 and y < size_y - 2:
        crds.add((y + 2, x - 1))
    if x > 1 and y < size_y - 1:
        crds.add((y + 1, x - 2))
    if x < size_x - 1 and y < size_y - 2:
        crds.add((y + 2, x + 1))
    if x < size_x - 2 and y < size_y - 1:
        crds.add((y + 1, x + 2))
    return crds


figures_threat = {
    KING: king_threat,
    ROOK: rook_threat,
    BISHOP: bishop_threat,
    QUEEN: queen_threat,
    KNIGHT: knight_threat
}
