__author__ = 'stafi'

import datetime
import chess2, view

# size_x = 6
# size_y = 9
# figs = {
#     chess2.king: 2,
#     chess2.queen: 1,
#     chess2.bishop: 1,
#     chess2.rook: 1,
#     chess2.knight: 1
# }

# size_x = 4
# size_y = 4
# figs = {
#    chess2.king: 0,
#    chess2.queen: 0,
#    chess2.bishop: 0,
#    chess2.rook: 2,
#    chess2.knight: 4
# }

size_x = 6
size_y = 6
figs = {
   chess2.king: 2,
   chess2.queen: 1,
   chess2.bishop: 0,
   chess2.rook: 1,
   chess2.knight: 1
}


def main():
    time1 = datetime.datetime.now()
    print("Start time: ", time1)
    fig_list = chess2.figs_as_list(figs)
    root_brd = chess2.create_empty_board(size_x, size_y)
    brds = chess2.place_figs_on_brd(fig_list, root_brd, size_x, size_y)
    # for brd in brds:
    #     view.print_board(chess2.unpack_board(brd, size_x, size_y))
    print("Number of boards: ", len(brds))
    print("Execution time: ", datetime.datetime.now() - time1)

main()