import figures

view_figures = {
    figures.KING: "K",
    figures.QUEEN: "Q",
    figures.BISHOP: "B",
    figures.KNIGHT: "N",
    figures.ROOK: "R",
    figures.EMPTY: "0",
}

# Prints board contents to console
def print_board(brd):
    if len(brd) > 0:
        for row in brd: print("|".join([view_figures[f] for f in row]))
        print("--" * (len(brd[0])))


# Compacts board presentation (dictionary) for storing in set
# The board is stored as tuple, which consists of coordinates followed by figure type:
#   y1, x1, figure1, y2, x2, figure2, ..., yN, xN, figureN
def pack(fig_data):
    packed = ()
    for crds in sorted(fig_data.keys()):
        y, x = crds
        packed += y, x, fig_data[crds]
    return packed


# Unpacks board from compact presentation and return list of lists
# See pack_board for information on compact board presentation
def unpack(packed, size_y, size_x):
    brd = [[figures.EMPTY for i in range(size_x)] for j in range(size_y)]
    for i in range(len(packed) // 3):
        y = packed[i * 3]
        x = packed[i * 3 + 1]
        f = packed[i * 3 + 2]
        brd[y][x] = f
    return brd


# Function tries to put list of figures on board and returns the set of distinct packed boards where all figures are put on board
def place_figs(figs_list, size_y, size_x):
    parent_fig_data = dict()
    parent_threat = set()
    return internal_place_figs(figs_list, size_y, size_x, parent_fig_data, parent_threat)


# Function tries to put list of figures on board and returns the set of distinct packed boards where all figures are put on board
# The function call itself recursively to try all the figures
def internal_place_figs(figs_list, size_y, size_x, parent_fig_data, parent_threat):
    brds = set()
    parent_figs_crds = parent_fig_data.keys()
    if len(figs_list) > 0:
        fig = figs_list[0]
        child_figs = figs_list[1:]
        for y in range(size_y):
            for x in range(size_x):
                cur_fig = (y, x)
                if cur_fig not in parent_figs_crds and cur_fig not in parent_threat:
                    cur_threat = figures.figures_threat[fig](y, x, size_y, size_x)
                    if not cur_threat.intersection(parent_figs_crds):
                        threat = parent_threat | cur_threat
                        fig_data = parent_fig_data.copy()
                        fig_data[cur_fig] = fig
                        if len(child_figs) > 0:
                            brds |= internal_place_figs(child_figs, size_y, size_x, fig_data, threat)
                        else:
                            brds |= {pack(fig_data)}
    return brds