#!/usr/bin/env python

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)

print(next(I1))
print(next(I2))

print(next(I1))                     # Lists support multiple iterators
print(next(I1))

print(next(I2))
print(next(I2))


