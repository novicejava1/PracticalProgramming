#!/usr/bin/env python

myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
print(myfile.readline())
print(myfile.readline())

print(open('myfile.txt').read())

for line in open('myfile.txt'):             # easiest to code, good on memory use
    print(line, end='')
