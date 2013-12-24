import figures
import datetime


# Returns map of (figures: counts) as list
def figs_as_list(figs):
    fig_list = []
    for k, v in figs.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


def place_figs(figs, brds, parent_fig_data, parent_threat_data, size_y, size_x):
    brds = set()
    if len(figs) > 0:
        fig = figs[0]
        child_figs = figs[1:]
        for y in range(size_y):
            for x in range(size_x):
                if (y, x) not in parent_threat_data:
                    threat = figures.figures_threat[fig](y, x, size_y, size_x)
                    if len(threat.intersection(parent_fig_data.viewkeys())) == 0:
                        threat_data = parent_threat_data | threat
                        fig_data = parent_fig_data.items()
                        fig_data[(y, x)] = fig
                        if len(child_figs) > 0:
                            place_figs(child_figs, brds, fig_data, threat_data, size_y, size_x)
                        else:
                            brds.add(sorted(fig_data))


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
    fig_list = figs_as_list(figs)
    brds = set()
    place_figs(fig_list, brds, dict(), set(), size_y, size_x)
    time2 = datetime.datetime.now()

    # Uncomment 2 lines below to see constructed boards
    # for brd in brds:
    #     chess.print_board(chess.unpack_board(brd, size_x, size_y))

    print("Number of boards: ", len(brds))
    print("Execution time: ", time2 - time1)

main()