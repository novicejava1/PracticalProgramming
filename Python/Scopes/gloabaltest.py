#!/usr/bin/env python

X = 88

def func():
    global X                    # defines a global variable
    X = 99

func()
print(X)

y, z = 1, 2

def all_global():
    global x
    x = y + z                   # x is declared as global and assigned a value 

all_global()
print(x)
