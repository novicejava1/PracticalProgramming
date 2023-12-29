#!/usr/bin/env python

spam = 'Spam'                           # simple assigment

print(spam)

spam, ham = 'yum', 'YUM'                # tuple unpacking

print(spam)
print(ham)

[spam, ham] = ['yum', 'YUM']            # list unpacking

print(spam)
print(ham)

a, b, c, d = 'spam'                     # sequence assignment

print(a, b, c, d)

a, *b = 'spam'                          # extended sequence unpacking

print(a)
print(b)

spam = ham = 'lunch'                    # multiple target assignment

print(spam)
print(ham)

spam = 18
spam += 42                              # augmented assignment

print(spam)

