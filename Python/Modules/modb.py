#!/usr/bin/env python

X = 11

import moda
moda.f()                    # Sets moda.X, not this file's X
print(X, moda.X)