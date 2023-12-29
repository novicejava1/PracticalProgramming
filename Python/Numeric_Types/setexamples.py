#!/usr/bin/env python

x = set('abcde')
y = set('bdxyz')

print(x)
print(y)

print(x - y)
print(x | y)
print(x & y)
print(x ^ y)


name = set('Python')
description = set('Hello Python')

print(name < description)           # name is subset of description
print(name > description)           # name is superset of description or not

a = {1, 2, 3, 4}
print(type(a))
print(a)
