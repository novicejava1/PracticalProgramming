#!/usr/bin/env python

res = [ord(x) for x in 'spam']                  # call in built function

print(res)

expo = [x ** 2 for x in range(10)]              # equivalent to map. call an expression

print(expo)

even = [x for x in range(5) if x % 2 == 0]      # equivalent to filter

print(even)

evenexpo = [x ** 2 for x in range(10) if x % 2 == 0]       # equivalent to filter and map

print(evenexpo)

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]   # nested for loop in comprehension

print(res)