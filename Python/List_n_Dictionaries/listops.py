#!/usr/bin/env python

l1 = [2, 3, 4]
l2 = [12, 13, 14]

print(len(l1))
print(len(l2))

print(l1 + l2)              # concatenation

print(l1 * 2)               # repetition

for i in l1:
    print(i, end='\n')

l3 = [x ** 2 for x in l1]
print(l3)

l4 = [-1, -2, 0, 1, 2]

maplist = list(map(abs, l4))
print(maplist)

L = ['spam', 'Spam', 'SPAM!']

print(L[2])
print(L[-1])
print(L[1:])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

L = [1, 2, 3]
L[1:2] = [4, 5]
print(L)