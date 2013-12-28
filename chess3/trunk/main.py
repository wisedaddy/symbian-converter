__author__ = 'stafi'

import board
import figures
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
    figs_dict = {
        figures.KING: 2,
        figures.QUEEN: 1,
        figures.BISHOP: 1,
        figures.ROOK: 1,
        figures.KNIGHT: 1
    }
    time1 = datetime.datetime.now()
    print("Start time: ", time1)
    brds = board.place_figs(figures.figs_as_list(figs_dict), size_y, size_x)
    time2 = datetime.datetime.now()
    #Uncomment 2 lines below to see constructed boards
    #for brd in brds:
    #    board.print_board(board.unpack(brd, size_x, size_y))
    print("Number of boards: ", len(brds))
    print("Execution time: ", time2 - time1)

main()