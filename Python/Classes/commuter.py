#!/usr/bin/env python

class Commuter2:

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    def __radd__(self, other):
        return self.__add__(other)                      # Call __add__ explicitly
    

class Commuter3:

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other                         # Swap order and re-add

    def __radd__(self, other):
        return self + other
    

class Commuter4:

    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    __radd__ = __add__


if __name__ == '__main__':

    X = Commuter2(2)
    aresult = X + 2
    print(aresult)
    rresult = 2 + X
    print(rresult)

    X = Commuter3(3)
    aresult = X + 2
    print(aresult)
    rresult = 2 + X
    print(rresult)

    X = Commuter4(4)
    aresult = X + 2                         # X.__add__(2)
    print(aresult)
    rresult = 2 + X                         # X.__radd__(2)
    print(rresult)