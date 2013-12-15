__author__ = 'stafi'


def check_king_place_allowed(brd, x, y, size_x, size_y):
    if y > 0 and brd[y - 1][x] != 0: return 0
    if y < size_y - 1 and brd[y + 1][x] != 0: return 0
    if x > 0:
        if brd[y][x - 1] != 0: return 0
        if y > 0 and brd[y - 1][x - 1] != 0: return 0
        if y < size_y - 1 and brd[y + 1][x - 1] != 0: return 0
    if x < size_x - 1:
        if brd[y][x + 1] != 0: return 0
        if y > 0 and brd[y - 1][x + 1] != 0: return 0
        if y < size_y - 1 and brd[y + 1][x + 1] != 0: return 0
    return 1


def check_rook_place_allowed(brd, x, y, size_x, size_y):
    row = brd[y]
    for col in range(size_x):
        if col != x and row[col] != 0:
            return 0
    for row in range(size_y):
        if row != y and brd[row][x] != 0:
            return 0
    return 1


def check_bishop_place_allowed(brd, x, y, size_x, size_y):
    x1 = x - min(x, y)
    y1 = y - min(x, y)
    end = 0
    i = 0
    while not end:
        if y1 + i >= size_y or x1 + i >= size_x:
            end = 1
        else:
            if x != x1 + i and y != y1 + i and brd[y1 + i][x1 + i] != 0:
                return 0
            i += 1

    x1 = x - min(x, size_y - y - 1)
    y1 = y - min(x, size_y - y - 1)
    end = 0
    i = 0
    while not end:
        if y1 - i < 0 or x1 + i >= size_x:
            end = 1
        else:
            if (size_y - 1 - y1 - i) != y and (x1 + i) != x and brd[size_y - 1 - y1 - i][x1 + i] != 0:
                return 0
            i += 1
    return 1


def check_queen_place_allowed(brd, x, y, size_x, size_y):
    if not check_bishop_place_allowed(brd, x, y, size_x, size_y):
        return 0
    for row_idx in range(size_y):
        if row_idx != y and brd[row_idx][x] != 0: return 0
    row = brd[y]
    for col_idx in range(size_x):
        if col_idx != x and row[col_idx] != 0: return 0
    return 1


def check_knight_place_allowed(brd, x, y, size_x, size_y):
    if x > 0 and y > 1:
        if brd[y - 2][x - 1] != 0: return 0
    if x > 1 and y > 0:
        if brd[y - 1][x - 2] != 0: return 0

    if x < size_x - 1 and y > 1:
        if brd[y - 2][x + 1] != 0: return 0
    if x < size_x - 2 and y > 0:
        if brd[y - 1][x + 2] != 0: return 0

    if x > 0 and y < size_y - 2:
        if brd[y + 2][x - 1] != 0: return 0
    if x > 1 and y < size_y - 1:
        if brd[y + 1][x - 2] != 0: return 0

    if x < size_x - 1 and y < size_y - 2:
        if brd[y + 2][x + 1] != 0: return 0
    if x < size_x - 2 and y < size_y - 1:
        if brd[y + 1][x + 2] != 0: return 0
    return 1

