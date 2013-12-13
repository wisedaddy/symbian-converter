__author__ = 'stafi'

import copy

x = 5
y = 5
brd = [[0 for xindex in range(x)] for yindex in range(y)]
brd_copy = copy.deepcopy(brd)
brd[3][3]=1
print(brd)
print(brd_copy)