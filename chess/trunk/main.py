__author__ = 'stafi'

import datetime
import chess, board

# Main entry point
# size_x, size_y and figs should be defined inside this function
def main():
    # The size of board
    # Number of columns
    size_x = 6
    # Number of rows
    size_y = 9
    # The figures and quantity of each figure which need to be placed on board
    figs = {
        board.king: 2,
        board.queen: 1,
        board.bishop: 1,
        board.rook: 1,
        board.knight: 1
    }

    time1 = datetime.datetime.now()
    print("Start time: ", time1)
    fig_list = chess.figs_as_list(figs)
    root_brd = chess.create_empty_board(size_x, size_y)
    brds = chess.place_figs_on_brd(fig_list, root_brd, size_x, size_y)
    time2 = datetime.datetime.now()

    # Uncomment 2 lines below to see constructed boards
    # for brd in brds:
    #     chess.print_board(chess.unpack_board(brd, size_x, size_y))

    print("Number of boards: ", len(brds))
    print("Execution time: ", time2 - time1)

main()
