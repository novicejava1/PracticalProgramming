#!/usr/bin/env python

def tester(start):
    state = start                       # Each call gets its own state
    def nested(label):
        nonlocal state                  # Remembers state in enclosing scope
        print(label, state)
        state += 1                      # Allowed to change it if nonlocal
    return nested

F = tester(0)
print(F('spam'))
# print(F.state)
