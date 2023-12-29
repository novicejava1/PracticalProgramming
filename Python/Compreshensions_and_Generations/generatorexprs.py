#!/usr/bin/env python

G = (x ** 2 for x in range(4))

print(G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
# print(next(G))                      # stopiteration exception is called

L = list((x ** 2 for x in range(4)))    # wrapping a generator expression in a list built-in call to force it to produce all its results in a list at once
print(L)    