__author__ = 'stafi'

import chess, view

size_x = 8
size_y = 8
figs = {
    chess.king: 0,
    chess.queen: 2,
    chess.bishop: 0,
    chess.knight: 0,
    chess.rook: 0}


print("Started")

fig_list = chess.figs_as_list(figs)
root_brd = chess.create_empty_board(size_x, size_y)
brds = chess.place_figs_on_brd(fig_list, root_brd, size_x, size_y, 0)
for brd in brds:
    view.print_board(brd)

print("Done")