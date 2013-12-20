__author__ = 'stafi'

import sys

packed = ()
for i in range(6):
    x = 10
    y = 10
    f = 1
    packed = packed + ((y, x, f),)
    #packed += x, y, f
print(sys.getsizeof(packed))
print(sys.getsizeof("K"))
print(sys.getsizeof(b"K"))