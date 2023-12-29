#!/usr/bin/env python

f = lambda x, y, z: print(x + y + z)

f('spam', 'ham', 'jam')

x = (lambda a="fee", b="fie", c="foe": print(a + b + c))

x('wee')
