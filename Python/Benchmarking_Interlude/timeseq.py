#!/usr/bin/env python

"""
Test the relative speed of iteration tool alternatives.
"""

import sys, timer
reps = 10000
repslist = list(range(reps))

def forloop():                              # plain for loop function
    res = []
    for i in repslist:
        res.append(abs(i))
    return res

def listcomp():                             # use of list comprehension        
    return [abs(x) for x in repslist]

def mapCall():                              # use of map
    return list(map(abs, repslist))

def genExpr():                                 # use of generator expre
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)

for test in (forloop, listcomp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print ('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))

