import figures

view_figures = {
    figures.king: "K",
    figures.queen: "Q",
    figures.bishop: "B",
    figures.knight: "N",
    figures.rook: "R",
    figures.empty: "0",
    figures.threat: "T"
}

# Returns map of (figures: counts) as list
def figs_as_list(figs):
    fig_list = []
    for k, v in figs.items():
        for i in range(v):
            fig_list.append(k)
    return fig_list


# Prints board contents to console
def print_board(brd):
    if len(brd) > 0:
        for row in brd: print("|".join([view_figures[f] for f in row]))
        print("--" * (len(brd[0])))


def pack(fig_data):
    packed = ()
    for crds in sorted(fig_data.keys()):
        (y, x) = crds
        packed += y, x, fig_data[crds]
    return packed


def unpack(packed, size_y, size_x):
    brd = [[figures.empty for xindex in range(size_x)] for yindex in range(size_y)]
    for i in range(len(packed)//3):
        y = packed[i*3]
        x = packed[i*3+1]
        f = packed[i*3+2]
        brd[y][x] = f
    return brd


def place_figs(figs, brds, size_y, size_x, parent_fig_data = dict(), parent_threat_data = set()):
    if len(figs) > 0:
        fig = figs[0]
        child_figs = figs[1:]
        for y in range(size_y):
            for x in range(size_x):
                parent_figs_crds = parent_fig_data.keys()
                current_fig_crds = (y, x)
                if current_fig_crds not in parent_threat_data and current_fig_crds not in parent_figs_crds:
                    threat = figures.figures_threat[fig](y, x, size_y, size_x)
                    if len(threat.intersection(parent_figs_crds)) == 0:
                        threat_data = parent_threat_data | threat
                        fig_data = parent_fig_data.copy()
                        fig_data[current_fig_crds] = fig
                        if len(child_figs) > 0:
                            place_figs(child_figs, brds, size_y, size_x, fig_data, threat_data)
                        else:
                            brds.add(pack(fig_data))
