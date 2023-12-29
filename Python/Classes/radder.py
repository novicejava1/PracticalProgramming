#!/usr/bin/env python

class Adder:

    def __init__(self, value = 0) -> None:
        self.data = value

    def __add__(self, other):
        return self.data + other
    
    def __radd__(self, other):
        print('radd', self.data, other)
        return other + self.data
    

X = Adder(5)
print(X + 5)
print(5 + X)                    # not supported if instance is on the right side of the operator. Works only with radd
