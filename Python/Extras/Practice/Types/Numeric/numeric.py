#!/usr/bin/env python

a = 34
b = 4.5678

print(a + b)
print(a * b)
print(a - b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)

print (a + b , a - 1)

if a and b: 
	print("Its true")

print( b / 2 + a)

# Stromg format expression
print('%e' % b)

# floating point format
print('%4.2f' % b)

# String format method
print('{0:4.2f}'.format(b))
