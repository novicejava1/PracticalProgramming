#!/usr/bin/env python

def gensquares(N):
    for i in range(N):
        yield i ** 2                    # Resume here later

nextVal = gensquares(5)                 # Resume the function

print(nextVal)                          # generator object returned

print("nextVal: ", next(nextVal))
print("nextVal: ", next(nextVal))
print("nextVal: ", next(nextVal))
print("nextVal: ", next(nextVal))
print("nextVal: ", next(nextVal))


for i in nextVal:
    print(i)

for i in gensquares(5):                 # Resume the function
    print(i)                            # Print last yielded value