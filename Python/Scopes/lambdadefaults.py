#!/usr/bin/env python

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)               # i retails the last value  4 for each function generated
    return acts                                     # enclosing scope variable is looked up when the nested functions are later called

acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)          # defaults are evaluated when the nested function is created (not when it’s later called
    return acts

acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))


