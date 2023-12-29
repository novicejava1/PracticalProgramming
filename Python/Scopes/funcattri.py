#!/usr/bin/env python

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(42)
F('spam')
F('ham')
print(F.state)

