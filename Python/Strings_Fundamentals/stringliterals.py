#!/usr/bin/env python

a = 'shrubbery'
b = "shrubbery"

print(a, b)

x = 'knight"s'
y = "knight's"

print(x, y)

c = 'knight\'s'
d = "knight\"s"

print(c, d)

s = 'a\nb\tc'

print(len(s))
print(s)

s = 'a\0b\0c'

print(s)

s = '\x01'

print(s)

s = "s\tp\na\x00m"

print(s)

path = r'C:\new\text.dat'
print(path)

path = 'C:\\new\\text.dat'
print(path)


