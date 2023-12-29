#!/usr/bin/env python

def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

L = [1, 2, 3, 4]
value = mysum(L)

print(value)

print(sum(L))

L = [1, 2, 3, 4, 5]

sum = 0

for x in L: sum += x

print(sum)