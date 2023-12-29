#!/usr/bin/env python

def intersect(seq1, seq2):
    x = [x for x in seq1 if x in seq2]
    return x

s1 = "SPAM"
s2 = "SCAM"
str1 = intersect(s1, s2)
print(str1)

x = intersect([1, 2, 3], (1, 4))
print(x)