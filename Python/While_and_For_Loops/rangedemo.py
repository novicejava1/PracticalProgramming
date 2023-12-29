#!/usr/bin/env python

for i in range(3):
    print(i, 'Pythons')

for i in range(0, 10, 2):
    print(i, 'Pythons')

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]
    print(X, end=' ')

print("\n")

S = 'abcdefghijk'               
for i in range(0, len(S), 2): print(S[i], end=' ')              # skip alternate items
print("\n")
for c in S[::2]: print(c, end=' ')                              # simpler form