#!/usr/bin/env python

y = 17
x = y // 2
print("x:" + str(x))
print("y:" + str(y))
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')