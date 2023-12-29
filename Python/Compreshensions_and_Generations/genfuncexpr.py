#!/usr/bin/env python

G = (c * 4 for c in 'SPAM')                 # Generator expression
genexpr = list(G)
print(genexpr)

def timesfour(S):                           # Generator function
    for c in S:
        yield c * 4

G = timesfour('spam')   

print(list(G))

G = (c * 4 for c in 'SPAM')

if iter(G) is G:
    print("Both are same")


G = (c * 4 for c in 'SPAM')

I1 = iter(G)
print(next(I1))
print(next(I1))

I2 = iter(G)
print(next(I2))                             # Second iterator at same position!. Generators Are Single-Iteration Objects

