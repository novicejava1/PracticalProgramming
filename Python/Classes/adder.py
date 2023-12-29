#!/usr/bin/env python

class adder:

    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        self.data += other
        return self.data
    
class addrepr(adder):
    
    def __repr__(self):
        return 'addrepr(%s)' % self.data
    
class addstr(adder):

    def __str__(self):
        return '[Value: %s]' % self.data

X = adder(5)
Y = X + 5                               # same as X.__add__(5)

print(X)
print(X.data)
print(Y)

X = addrepr(5)
print(X)

X = addstr(3)
print(X)
X + 1
print(X)
print(str(X))
print(repr(X))