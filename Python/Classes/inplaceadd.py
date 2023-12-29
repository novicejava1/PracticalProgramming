#!/usr/bin/env python

class Number:

    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self
    
X = Number(5)
X += 1
print(X.val)

Y = Number([5])
Y += [2, 4]
print(Y.val)