#!/usr/bin/env python

x = 10

while x:
    x = x - 1
    if x % 2 != 0: continue
    print(x, end=' ')

x = 10
while x:
    x = x - 1
    if x % 2 == 0:
        print(x, end=' ')
