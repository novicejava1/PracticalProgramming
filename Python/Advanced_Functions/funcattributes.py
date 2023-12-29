#!/usr/bin/env python

def func(message):
    print(message)

func("Hello Python")
func.state = 1                                  # count and state are user defined function attributes
func.count = 0

print(dir(func))