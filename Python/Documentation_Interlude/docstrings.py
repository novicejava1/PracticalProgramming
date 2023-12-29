#!/usr/bin/env python

"""
This is a simple module documentation
on how to use it
"""

spam = 40

def square(x):
    """
    This is simple documentation
    for the square function
    """

    return x ** 2                       # square of x

class Employee:
    """
    This is a simple class documentation
    for the Employee
    """
    pass

print(square(spam))
print(square.__doc__)