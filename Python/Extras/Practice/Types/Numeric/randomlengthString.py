#!/usr/bin/env python

import random
import string

keystring = []
s = []
for i in range(40):
	s = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase))
	print(s, end='')
print("\n")
data2 = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(40))
data3 = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=40))

print(data2)
print(data3)




