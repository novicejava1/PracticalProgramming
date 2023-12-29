#!/usr/bin/env python

def maker(N):
    def action(X):                          # make and return action
        return X ** N                       # action retains N from enclosing scope
    return action

f = maker(3)                                # returns action generated function with N = 3
cuberes = f(2)                               # is basically calling action(3) with N = 3

g = maker(2)
squareres = g(2)

print(cuberes)
print(squareres)