#!/usr/bin/env python

class tester():
    def __init__(self, start) -> None:
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state += 1

F = tester(0)                               # Create instance, invoke __init__
F.nested('spam')
F.nested('ham')

G = tester(42)
G.nested('toast')
G.nested('bacon')