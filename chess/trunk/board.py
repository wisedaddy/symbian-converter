__author__ = 'stafi'

king = 1
queen = 2
bishop = 3
knight = 4
rook = 5
empty = 9
threat = 0

# Checks whether the spot on board is not occupied by any figure
def free_of_figures(brd, y, x):
    return brd[y][x] == empty or brd[y][x] == threat


# Checks whether the spot on board is free of any figures and is not under attack by any other figures
def free_of_threat(brd, y, x):
    return brd[y][x] == empty


# Checks whether the spot on board is not under attack of any other figures.
# If teh spot is occupied - function returns 0
# Otherwise, it is marked as under attack (if not marked yet)
def check_and_mark_threat(brd, y, x):
    state = brd[y][x]
    if state == empty:
        brd[y][x] = threat
        return 1
    elif state == threat:
        return 1
    else:
        return 0


# Checks whether ROOK can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
def check_and_mark_rook_threat(brd, x, y, size_x, size_y):
    for col in range(size_x):
        if col != x and not check_and_mark_threat(brd, y, col):
            return 0
    for row in range(size_y):
        if row != y and not check_and_mark_threat(brd, row, x):
            return 0
    return 1


# Checks whether BISHOP can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
def check_and_mark_bishop_threat(brd, x, y, size_x, size_y):
    min_x_y = min(x, y)
    x1 = x - min_x_y
    y1 = y - min_x_y
    i = 0
    while y1 + i < size_y and x1 + i < size_x:
        if x1 + i != x and y1 + i != y and not check_and_mark_threat(brd, y1 + i, x1 + i):
            return 0
        i += 1
    min_x_y = min(x, size_y - y - 1)
    x1 = x - min_x_y
    y1 = y + min_x_y
    i = 0
    while y1 - i >= 0 and x1 + i < size_x:
        if x1 + i != x and y1 - i != y and not check_and_mark_threat(brd, y1 - i, x1 + i):
            return 0
        i += 1
    return 1


# Checks whether KING can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
# The place where KING is placed is marked with corresponding value
def put_king(brd, x, y, size_x, size_y):
    if y > 0:
        if not check_and_mark_threat(brd, y - 1, x):
            return 0
    if y < size_y - 1:
        if not check_and_mark_threat(brd, y + 1, x):
            return 0
    if x > 0:
        if not check_and_mark_threat(brd, y, x - 1):
            return 0
        if y > 0:
            if not check_and_mark_threat(brd, y - 1, x - 1):
                return 0
        if y < size_y - 1:
            if not check_and_mark_threat(brd, y + 1, x - 1):
                return 0
    if x < size_x - 1:
        if not check_and_mark_threat(brd, y, x + 1):
            return 0
        if y > 0:
            if not check_and_mark_threat(brd, y - 1, x + 1):
                return 0
        if y < size_y - 1:
            if not check_and_mark_threat(brd, y + 1, x + 1):
                return 0
    brd[y][x] = king
    return 1


# Checks whether ROOK can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
# The place where ROOK is placed is marked with corresponding value
def put_rook(brd, x, y, size_x, size_y):
    if not check_and_mark_rook_threat(brd, x, y, size_x, size_y):
        return 0
    brd[y][x] = rook
    return 1


# Checks whether BISHOP can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
# The place where BISHOP is placed is marked with corresponding value
def put_bishop(brd, x, y, size_x, size_y):
    if not check_and_mark_bishop_threat(brd, x, y, size_x, size_y):
        return 0
    brd[y][x] = bishop
    return 1


# Checks whether QUEEN can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
# The place where QUEEN is placed is marked with corresponding value
def put_queen(brd, x, y, size_x, size_y):
    # queen moves like rook
    if not check_and_mark_rook_threat(brd, x, y, size_x, size_y):
        return 0
        # and like bishop
    if not check_and_mark_bishop_threat(brd, x, y, size_x, size_y):
        return 0
    brd[y][x] = queen
    return 1


# Checks whether KNIGHT can be placed at specified spot.
# The spots that become under attack are marked accordingly.
# If these spots contain any figures, the function returns 0 (in this case the board is not usable for future processing)
# The place where KNIGHT is placed is marked with corresponding value
def put_knight(brd, x, y, size_x, size_y):
    if x > 0 and y > 1:
        if not check_and_mark_threat(brd, y - 2, x - 1):
            return 0
    if x > 1 and y > 0:
        if not check_and_mark_threat(brd, y - 1, x - 2):
            return 0

    if x < size_x - 1 and y > 1:
        if not check_and_mark_threat(brd, y - 2, x + 1):
            return 0
    if x < size_x - 2 and y > 0:
        if not check_and_mark_threat(brd, y - 1, x + 2):
            return 0

    if x > 0 and y < size_y - 2:
        if not check_and_mark_threat(brd, y + 2, x - 1):
            return 0
    if x > 1 and y < size_y - 1:
        if not check_and_mark_threat(brd, y + 1, x - 2):
            return 0

    if x < size_x - 1 and y < size_y - 2:
        if not check_and_mark_threat(brd, y + 2, x + 1):
            return 0
    if x < size_x - 2 and y < size_y - 1:
        if not check_and_mark_threat(brd, y + 1, x + 2):
            return 0
    brd[y][x] = knight
    return 1


func_put_fig = {
    king: put_king,
    rook: put_rook,
    bishop: put_bishop,
    queen: put_queen,
    knight: put_knight
}
