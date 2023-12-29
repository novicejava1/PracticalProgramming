#!/usr/bin/env python

line = 'aa bbb c'

joined = ''.join(x for x in line.split() if len(x) > 1)         # list comprehension with filtering data

print(joined)