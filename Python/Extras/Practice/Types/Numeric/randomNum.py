#!/usr/bin/env python

import random

# Random number between 0 and 1
print(random.random())

# Random number between 1 to 10
print(random.randint(1, 10))

# Random choice
print(random.choice(['Python', 'Java', 'Docker']))

# Shuffle the values
data = ['Ted', 'Bed', 'Led', 'Sed']
random.shuffle(data)
print(data)
