#!/usr/bin/env python

def maker(N):
    return lambda X: X ** N                 # lambda function retain state too

h = maker(2)
result = h(2)

print(result)