#!/usr/bin/env python

def sumtree(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total = total + x
        else:
            total = total + sumtree(x)
    return total

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))