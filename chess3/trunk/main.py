__author__ = 'stafi'

import chess3, figures
import datetime


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
        figures.king: 2,
        figures.queen: 1,
        figures.bishop: 1,
        figures.rook: 1,
        figures.knight: 1
    }

    time1 = datetime.datetime.now()
    print("Start time: ", time1)
    fig_list = chess3.figs_as_list(figs)
    brds = set()
    chess3.place_figs(fig_list, brds, size_y, size_x)
    time2 = datetime.datetime.now()

    # Uncomment 2 lines below to see constructed boards
    #for brd in brds:
    #     chess3.print_board(chess3.unpack(brd, size_x, size_y))

    print("Number of boards: ", len(brds))
    print("Execution time: ", time2 - time1)

main()