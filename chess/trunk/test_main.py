__author__ = 'stafi'

import datetime, sys
import chess, board, main

# size_x = 6
# size_y = 9
# figs = {
#     chess2.king: 2,
#     chess2.queen: 1,
#     chess2.bishop: 1,
#     chess2.rook: 1,
#     chess2.knight: 1
# }


size_x = 6
size_y = 6
figs = {
   board.king: 1,
   board.queen: 1,
   board.bishop: 1,
   board.rook: 1,
   board.knight: 1
}


#size_x = 4
#size_y = 4
#figs = {
#    chess2.king: 0,
#    chess2.queen: 0,
#    chess2.bishop: 0,
#    chess2.rook: 2,
#    chess2.knight: 4
#}

def main():
    time1 = datetime.datetime.now()
    print("Start time: ", time1)
    fig_list = chess.figs_as_list(figs)
    root_brd = chess.create_empty_board(size_x, size_y)
    brds = chess.place_figs_on_brd(fig_list, root_brd, size_x, size_y)
    time2 = datetime.datetime.now()
    for brd in brds: main.print_board(chess.unpack_board(brd, size_x, size_y))
    print("Object size: ", sys.getsizeof(brds))
    print("Number of boards: ", len(brds))
    print("Execution time: ", time2 - time1)

main()