#!/usr/bin/env python

s = 'This is a long string with python in it'

print(s[0])
print(s[4:8])
print(s[1:])
print(s[:-1])
print(s[:])

print(len(s))
print(s[0:39:2])            # get string character with a step of 2
print(s[::2])               # same as above with first and second index being 0 and length of the string

print(s[::-1])              # basically prints the string in reverse order

s = 'spam'
print(s[slice(1,3)])        # slicing with slice indexing object

print(ord('s'))             # character code conversion from character to binary code
print(chr(115))             # convert from character code to character

B = '1101'
print(int(B, 2))


B = '1101'
I = 0
while B != '':
    print('-' * 80)
    print(ord(B[0]))
    print(ord('0'))
    I = I * 2 + (ord(B[0]) - ord('0'))
    print(I)
    B = B[1:]
    print(B)
    print('-' * 80)

print('This is %d %s bird!' % (1, 'dead'))              # string format expression
print('That is {0} {1} bird!'.format(1, 'dead'))        # string format methods
