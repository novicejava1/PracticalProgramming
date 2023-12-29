#!/usr/bin/env python

seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)

seq = [1, 2, 3, 4]
a, *b = seq
# print(a)
# print(b)
print(a, b)

*a, b = seq
# print(a)
# print(b)
print(a, b)

a, *b, c = seq
print(a, b, c)

a, b, *c = seq
print(a, b, c)

a, *b = 'spam'
print(a, b)