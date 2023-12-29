#!/usr/bin/env python

D = {'c': 1, 'a': 2, 'b': 3}

Ks = D.keys()
# rint(Ks.sort())           # no sort method for dict keys views

Ks = list(Ks)
Ks.sort()
print(Ks)

D = {'b': 2, 'c': 3, 'a': 1}

Ks = D.keys()
for k in sorted(Ks): print(k, D[k])

D = {'b': 2, 'c': 3, 'a': 1}
for k in sorted(D): print(k, D[k])