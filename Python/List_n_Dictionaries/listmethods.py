#!/usr/bin/env python

L = ['eat', 'more', 'SPAM!']

L.append('GiveMore')

print(L)

L.extend(['Forest', 'Matters'])

print(L)

L.sort()

print(L)

L = ['abc', 'ABD', 'aBe']

L.sort(key=str.lower)

print(L)

L.sort(key=str.lower, reverse=True)

print(L)

L = ['abc', 'ABD', 'aBe']

sorted(L, key=str.lower, reverse=True)

L = ['abc', 'ABD', 'aBe']

x = [x.lower() for x in L]

print(x)

sortedx = sorted(x, reverse=True)

print(sortedx)

L = [1, 2]
L.extend([3, 4, 5])

print(L)

lastvalue = L.pop()

print(lastvalue)

L.reverse()

print(L)

print(list(reversed(L)))

L = ['spam', 'eggs', 'ham']

print(L.index('eggs'))

L.insert(1, 'toast')

print(L)

L.remove('eggs')

print(L)

print(L.count('spam'))

del L[1:]

print(L)