#!/usr/bin/env python

def func(a, b, c):
    return a + b + c

func(1, 2, 3)

def func(a: 'spam', b: (1, 10), c: float) -> int:
    return a + b + c

result = func(1, 2, 3)
print(result)

print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])
