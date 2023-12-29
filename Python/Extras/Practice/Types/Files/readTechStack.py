#!/usr/bin/env python

f = open('techstack.txt', 'r')

for eachLine in f.readlines():
	print(eachLine, end='')

print(dir(f))
f.close()


for line in open('techstack.txt', 'r'):
	print(line, end='')

print(dir(line))
