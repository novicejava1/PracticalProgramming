#!/usr/bin/env python

import operator
from functools import reduce

sum = reduce((lambda x, y: x + y), [1, 2, 3, 4])
prod = reduce((lambda x, y: x + y), [1, 2, 3, 4, 5])

print(sum, prod)

opersum = reduce(operator.add, [2, 4, 6])

print(opersum)