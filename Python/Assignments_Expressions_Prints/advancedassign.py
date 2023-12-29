#!/usr/bin/env python

string = 'SPAM'

a, b, c, d = string

print(a, d)

# a, b, c = string            # error as the number of values on right does match the left

a, b, c = string[0], string[1], string[2:]

print(a, b, c)

a, b, c = list(string[:2]) + [string[2:]]

print(a, b, c)

a, b = string[:2]
c = string[2:]

print(a, b, c)

(a, b), c = string[:2], string[2:]

print(a, b, c)

red, green, blue = range(3)                 # python equivalent of enumerated datatypes

print(red, green, blue)

for i in range(3):
    print(i)