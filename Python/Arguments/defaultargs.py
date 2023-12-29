#!/usr/bin/env python

def f(firstname, age=50, gender='male'):
    print(firstname, age, gender)

f(firstname='andy')
f('grant')
f('grant', age=24)