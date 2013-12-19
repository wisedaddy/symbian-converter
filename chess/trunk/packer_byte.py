__author__ = "stafi"

import board, chess

def pack_board(brd, size_x, size_y):
    packed = b''
    for y in range(size_y):
        for x in range(size_x):
            if not board.free_of_figures(brd, y, x):
                packed += bytes([y, x, ord(brd[y][x])])
    return packed


def unpack_board(packed, size_x, size_y):
    brd = chess.create_empty_board(size_x, size_y)
    for i in range(len(packed)//3):
        y = packed[i*3]
        x = packed[i*3+1]
        f = chr(packed[i*3+2])
        brd[y][x] = f
    return brd
