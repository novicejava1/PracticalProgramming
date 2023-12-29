#!/usr/bin/env python

counters = [1, 2, 3, 4]

def inc(x): return x + 10

result = list(map(inc, counters))

print(result)


result = list(map((lambda x: x + 3), counters))

print(result)

print(list(map(pow, [1, 2, 3], [2, 3, 4])))