#!/usr/bin/env python

D = dict(a=1, b=2, c=3)

K = D.keys()                    # creates view object for keys
V = D.values()                  # creates view object for values
I = D.items()                   # creates view object for items

print(K | {'x': 4})

# print(V & {'x': 4})             # values views are not set-like

print(D.keys() & D.keys())          # Intersect keys views

print(D.keys() & {'b'})              # Intersect keys and set

print(D.keys() & {'b': 1})         # Intersect keys and dict

print(D.keys() | {'b', 'c', 'd'})   # union of keys and sets

D = {'a': 1}

print(list(D.items()))              # items set like if hashable

print(D.items() | D.keys())         # Union view and view

print(D.items() | D)                # Union of view and dict which is a key by default

print(D.items() | {('c', 3), ('d', 4)})

print(dict(D.items() | {('c', 3), ('d', 4)}))   # print in dict format


