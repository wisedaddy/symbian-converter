__author__ = 'stafi'

import chess2


def free_of_figures(brd, y, x):
    return brd[y][x] == chess2.empty or brd[y][x] == chess2.threat


def free_of_threat(brd, y, x):
    return brd[y][x] == chess2.empty


def check_and_mark_threat(brd, y, x):
    if free_of_figures(brd, y, x):
        brd[y][x] = chess2.threat
        return 1
    else:
        return 0


def check_and_mark_fig(brd, y, x, fig):
    if free_of_threat(brd, y, x):
        brd[y][x] = fig
        return 1
    else:
        return 0


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
    if not check_and_mark_fig(brd, y, x, chess2.king):
        return 0
    return 1


def check_and_mark_rook_threat(brd, x, y, size_x, size_y):
    for col in range(size_x):
        if col != x and not check_and_mark_threat(brd, y, col):
            return 0
    for row in range(size_y):
        if row != y and not check_and_mark_threat(brd, row, x):
            return 0
    return 1


def check_and_mark_bishop_threat(brd, x, y, size_x, size_y):
    min_x_y = min(x, y)
    x1 = x - min_x_y
    y1 = y - min_x_y
    end = 0
    i = 0
    while not end:
        if y1 + i >= size_y or x1 + i >= size_x:
            end = 1
        else:
            cur_y, cur_x = y1 + i, x1 + i
            if cur_x != x and cur_y != y and not check_and_mark_threat(brd, cur_y, cur_x):
                return 0
            i += 1

    min_x_y = min(x, size_y - y - 1)
    x1 = x - min_x_y
    y1 = y + min_x_y
    end = 0
    i = 0
    while not end:
        if y1 - i < 0 or x1 + i >= size_x:
            end = 1
        else:
            if (y1 - i) != y and (x1 + i) != x and not check_and_mark_threat(brd, y1 - i, x1 + i):
                return 0
            i += 1
    return 1


def put_rook(brd, x, y, size_x, size_y):
    if not check_and_mark_rook_threat(brd, x, y, size_x, size_y):
        return 0
    if not check_and_mark_fig(brd, y, x, chess2.rook):
        return 0
    return 1


def put_bishop(brd, x, y, size_x, size_y):
    if not check_and_mark_bishop_threat(brd, x, y, size_x, size_y):
        return 0
    if not check_and_mark_fig(brd, y, x, chess2.bishop):
        return 0
    return 1


def put_queen(brd, x, y, size_x, size_y):
    if not check_and_mark_rook_threat(brd, x, y, size_x, size_y):
        return 0
    if not check_and_mark_bishop_threat(brd, x, y, size_x, size_y):
        return 0
    if not check_and_mark_fig(brd, y, x, chess2.queen):
        return 0
    return 1


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
    if not check_and_mark_fig(brd, y, x, chess2.knight):
        return 0
    return 1

