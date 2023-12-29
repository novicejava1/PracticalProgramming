#!?usr/bin/env python

L = list(range(-5, 5))

print(L)

postivenums = list(filter(lambda x: x > 0, L))

print(postivenums)

negativenums = list(filter(lambda x: x < 0, L))

print(negativenums)