#!/usr/bin/env python

X = 99

def f1():
    X = 88                                  # enclosing function variable
    def f2():
        nonlocal X                          # refering to enclosing function variable and changed data
        print(X)                            # remembers X in enclosing function
        X = "Changed!!"
        print(X)
    f2()
    print(X)

f1()
print(X)                                    # global scope variable
