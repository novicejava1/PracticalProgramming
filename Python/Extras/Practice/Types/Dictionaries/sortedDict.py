#!/usr/bin/env python

D = {'a': 10, 'b': 20, 'c': 30}

print(D)

for key in sorted(D):
	print(key, "=>", D[key])

if 'd' not in D:
	print("Missing key")
else:
	print("Available key")