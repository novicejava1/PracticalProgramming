#!/usr/bin/env python

def changer(a, b):
    a = 2
    b[0] = 'spam'                           # in place change for mutable object

X = 1
Y = ["ham", "spam"]

changer(X, Y)
print(X)
print(Y)