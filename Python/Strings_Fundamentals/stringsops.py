#!/usr/bin/env python

str1 = 'abc'
str2 = 'def'

print(len(str1))
print(len(str2))

print(str1 + str2)

str3 = 'spam!!'
print('-' * 80)
print(str3 * 4)
print('-' * 80)

myjob = 'hacker'
for c in myjob: print(c, end=' ')
if 'k' in myjob: print('Found')
