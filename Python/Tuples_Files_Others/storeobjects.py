#!/usr/bin/env python

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

print(str(D))
print(str(L))

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s, %s, %s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

data = open('datafile.txt', 'r')
print(data.read())
data.close()

data = open('datafile.txt', 'r')
for eachline in data:
    print(type(eachline), eachline)