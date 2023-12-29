#!/usr/bin/env python

X = 99                              # global scope variable

def func():                         # func global scope variable
    X = 88                          # local scope variable
    print("Local Scope X: " + str(X))

func()
print("Global Scope X: " + str(X))

