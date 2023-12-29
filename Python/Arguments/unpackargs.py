#!/usr/bin/env python

def func(a, b, c, d, e=1):
    print(a, b, c, d, e)

args = (1, 2)
args += (3, 4)

func(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4

func(**args)

func(*(1, 2), **{'d': 4, 'c': 3})

func(1, *(2, 3), **{'d': 4})

func(1, c=3, *(2,), **{'d': 4})

func(1, *(2, 3), d=4)

func(1, *(2,), c=3, **{'d':4})