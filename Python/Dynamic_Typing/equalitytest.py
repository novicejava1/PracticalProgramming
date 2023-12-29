#!/usr/bin/env python

L = [2, 3, 4]
M = [2, 3, 4]

print(L == M)               # tests the equality of the objects content
print(L is M)               # tests if both the objects references are same or not

X = 42
Y = 42

print(X == Y)               # tests the equality of the objects content
print(X is Y)               # tests if both the objects references are same or not. In this case its True because small integers and strings are cached and reused
