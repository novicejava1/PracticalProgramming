#!/usr/bin/env python

def f(a, b, c): print('%s, %s, and %s' % (a, b, c))

f(*range(3))
f(*(i for i in range(3)))               # unpack generator expressions


D = dict(a='Bob', b='dev', c=40.5)

f(a='Bob', b='dev', c=40.5)

f(**D)                                  # unpack dict key and value

f(*D)                                   # unpack key iterator
print(D.keys)

f(*D.values())                          # unpack view iterator
