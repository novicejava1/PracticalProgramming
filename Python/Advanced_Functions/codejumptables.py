#!/usr/bin/env python

L = [lambda x: x ** 2,                                  # lists or dictionaries of actions
     lambda x: x ** 3,
     lambda x: x ** 4]

print(L[0](1))
print(L[0](2))
print(L[0](3))

print(L[1](1))
print(L[1](2))
print(L[1](3))

print(L[2](1))
print(L[2](2))
print(L[2](3))

key = 'got'

dict1 = {'already': (lambda: 2 + 2),
        'got': (lambda: 2 * 4),
        'one': (lambda: 2 ** 6)
        }

print(dict1[key]())



