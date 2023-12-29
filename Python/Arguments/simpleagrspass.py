#!/usr/bin/env python

def f(a):
    print(a)                        # before the reference value is changed
    a = 99
    print(a)

b = 88
print(b)
f(b)
print(b)                            # b value after function call ends is the same
