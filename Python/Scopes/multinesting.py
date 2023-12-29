#!/usr/bin/env python

def f1():
    x = 99
    def f2():                               # better if you minimize nested function definitions for better readability and usability
        def f3():
            print(x)
        f3()
    f2()
f1()
