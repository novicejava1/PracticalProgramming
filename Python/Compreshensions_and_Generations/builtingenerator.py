#!/usr/bin/env python

D = {'a':1, 'b':2, 'c':3}
x1 = iter(D)

print(next(x1))
print(next(x1))
print(next(x1))

x1 = iter(D)

print(D[next(x1)])
print(D[next(x1)])
print(D[next(x1)])