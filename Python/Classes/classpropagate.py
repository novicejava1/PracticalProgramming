#!/usr/bin/env python

class Commuter5():

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, Commuter5):                # Type test to avoid object nesting
            other = other.val
        return Commuter5(self.val + other)              # Else + result is another Commuter
    
    def __radd__(self, other):
        return Commuter5(other + self.val)
    
    def __str__(self) -> str:
        return '<Commuter5: %s>' % self.val
    

X = Commuter5(88)
Y = Commuter5(99)

print(X.val)
print(Y.val)

print(X + 10)                       # call X.__add__(10)    # Result is another Commuter instance
print(10 + Y)

Z = X + Y                           # call X.__add__(Y), Y is an instance # Not nested: doesn't recur to __radd__
print(Z)