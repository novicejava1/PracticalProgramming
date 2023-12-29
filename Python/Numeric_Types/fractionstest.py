#!/usr/bin/env python

from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x, y)
print(x + y)
print(x - y)
print(x * y)

print(Fraction('.24'))
print(Fraction('1.25'))

a = 1 / 3.0
b = 4 / 6.0

print(a, b)
print(a + b)

a = Fraction(1, 3)
b = Fraction(4, 6)

print(a + b)

f = 2.5
z = Fraction(*f.as_integer_ratio())

print(z)
print(float(x))
print(float(z))
print(x + z)

print(Fraction.from_float(1.75))