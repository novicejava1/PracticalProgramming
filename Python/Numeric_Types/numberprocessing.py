#!/usr/bin/env python

import math
import random

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))

print(math.sqrt(144))

print(pow(2, 4))

print(sum([3, 3, 3, 3]))
print(min([3, 5, 1, 6, 3]))
print(max([3, 5, 1, 6, 3]))

print(random.random())
print(random.randint(1, 10))
print(random.choice([4, 6, 1, 3]))

suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)
print(suits)