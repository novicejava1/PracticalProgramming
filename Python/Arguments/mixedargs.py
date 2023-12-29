#!/usr/bin/env python

def f(a, *pargs, **kargs):
    print(a, pargs, kargs)

f(1, 2, 3, x=1, y=2)


def f(a='defaultval', *pargs, **kargs):
    print(a, pargs, kargs)

f(x=1, y=2)