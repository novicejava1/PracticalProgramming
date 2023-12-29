#!/usr/bin/env python

for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')

sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x
print(sum)

prod = 1
for item in [1, 2, 3, 4]: prod *= item
print(prod)

S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S: print(x, end=' ')
for x in T: print(x, end=' ')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

D = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in D.items():
    print(key, '=>', value)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)

for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)

for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:             # extended seq assign in loop
    print(a, b, c)