#!/usr/bin/env python

class Truth:
    def __bool__(self): return True

X = Truth()
if X: print('yes!')
print(bool(X))
