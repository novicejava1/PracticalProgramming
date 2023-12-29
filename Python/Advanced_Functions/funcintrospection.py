#!/usr/bin/env python

def func(a):
    b = 'spam'
    return b * a

func(8)
print(dir(func))

print(func.__name__)
print(func.__code__)

print(func.__code__.co_varnames)
print(func.__code__.co_argcount)