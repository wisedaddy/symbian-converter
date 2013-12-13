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
    x1 = x - min(x,y)
    y1 = y - min(x,y)
    end = 0
    i = 0
    while not end:
        if y1+i>=size_y or x1+i>=size_x:
            end = 1
        else:
            if brd[y1+i][x1+i] != 0:
                return 0
            i+=1

    x1 = x - min(x,size_y - y - 1)
    y1 = y - min(x,size_y - y - 1)
    end = 0
    i = 0
    while not end:
        if y1-i<0 or x1+i>=size_x:
            end = 1
        else:
            if brd[size_y-1-y1-i][x1+i] != 0:
                return 0
            i+=1
    return 1

def check_queen_place_allowed(brd, x, y, size_x, size_y):
    if not check_bishop_place_allowed(brd, x, y, size_x, size_y):
        return 0
    for f in [row[x] for row in brd]:
        if f == 0: return 0
    row = brd[y]
    for f in row:
        if f == 0: return 0