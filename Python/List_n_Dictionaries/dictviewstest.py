#!/usr/bin/env python

D = dict(a=1, b=2, c=3)

K = D.keys()                    # creates view object for keys
V = D.values()                  # creates view object for values
I = D.items()                   # creates view object for items

print(K)
print(V)
print(I)

print(list(K))
print(list(V))
print(list(I))

del D['a']                      # dynamically reflect future changes made to the dictionary after the view object has been created

print(list(K))
print(list(V))
print(list(I))

