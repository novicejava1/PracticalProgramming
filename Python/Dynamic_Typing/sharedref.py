#!/usr/bin/env python

import copy

a = 3
b = a
a = 'spam'

print(a)
print(b)

L1 = [2, 3, 4]
L2 = L1
L1 = 24

print(L1)
print(L2)

L1 = [2, 3, 4]
L2 = L1
L1[1] = 24

print(L1)
print(L2)

L1 = [2, 3, 4]
L2 = L1[:]                  # L2 is a copy of L1 and not the actual L1
L1[1] = 24

print(L1)
print(L2)

L1 = [2, 3, 4]
#L2 = copy.copy(L1)              # This is a shallow copy of L1 not copying the nested objects
L2 = copy.deepcopy(L1)          # L2 is a copy of L1 using the copy module
L1[1] = 32

print(L1)
print(L2)