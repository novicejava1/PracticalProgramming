#!/usr/bin/env python

def echo(message):
    print(message)

schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]

for func, arg in schedule:
    print(func)
    print(arg)
    func(arg)