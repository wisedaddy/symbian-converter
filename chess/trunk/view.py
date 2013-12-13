__author__ = 'stafi'

def print_board(brd):
    for yindex in range(len(brd)):
        row = brd[yindex]
        s = ''
        for el in row:
            s += '|'
            s += str(el)
            if el == len(row) - 1:
                s += '|'
        print(s)
        if yindex == len(brd) - 1:
            print('--' * len(row) + '-')
