#!/usr/bin/env python

def multiple(x, y):
    x = 2                               # Changes local names only
    y = [3, 4]
    return x, y                         # Return multiple new values in a tuple

X = 1
Y = ["spam", "jam"]
multiple(X, Y)                          # mutable object changes
print(X, Y)

X, Y = multiple(X, Y)                   # Assign results to caller's names. call by reference simulation             
print(X, Y)
