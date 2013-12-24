__author__ = 'stafi'

king = 1
queen = 2
bishop = 3
knight = 4
rook = 5
empty = 9
threat = 0

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


def rook_threat(y, x, size_y, size_x):
    crds = set()
    for col in range(size_x):
        if col != x:
            crds.add((y, col))
    for row in range(size_y):
        if row != y:
            crds.add((row, x))
    return crds


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


def queen_threat(y, x, size_y, size_x):
    crds = rook_threat(y, x, size_y, size_x) | bishop_threat(y, x, size_y, size_x)
    return crds


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
    king: king_threat,
    rook: rook_threat,
    bishop: bishop_threat,
    queen: queen_threat,
    knight: knight_threat
}
