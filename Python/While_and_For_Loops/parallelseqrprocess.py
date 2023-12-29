#!/usr/bin/env python

L1 = [1,2,3,4]
L2 = [5,6,7,8]

for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

print(list(map(ord, 'spam')))
      
res = []
for c in 'spam': res.append(ord(c))
print(res)