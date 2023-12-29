#!/usr/bin/env python

L, S = [1, 2, 3], 'spam'

for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L, end=' ')

for i in range(len(S)):
    X = S[i:] + S[:i]
    print(X, end=' ')