#!/usr/bin/env python

import random

print("Generate 5 digit random number")

for i in range(5):
    print(random.choice([0,1,2,3,4,5,6,7,8,9]), end='')

