#!/usr/bin/env python

def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    print(res)

scramble('spam')
scramble([2, 5, 3])

def genscramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq

print(list(genscramble('spam')))
print(list(genscramble([5, 1, 7])))

S = 'spam'
G = (S[i:] + S[:i] for i in range(len(S)))

print(list(G))