#!/usr/bin/env python

import sys
def gen():
    for i in range(10):
            X = yield i
            if X == 'Interrupt':
                  sys.exit(1)
              
            #print("Inside Generator: ", X)


G = gen()

print(next(G))
print(next(G))
print(next(G))
# G.send('Interrupt')                          # generator advances to the next item. Basically we can interrupt the generator and exit
print(next(G))

for num in (x ** 2 for x in range(4)):       # next value is generator object is automatically iterated using iter protocol
      print('%s, %s' % (num, num / 2.0))

