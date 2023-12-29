#!/usr/bin/env python

T = ()                          # empty tuple

print(T)

T = (0,)                        # single item tuple

print(T)

T = (1.2, [1, 2], 'python')     # nested item tuple

print(T)

T1 = tuple(['s', 'p', 'a', 'm'])         # tuple creation using different form

print(T)

print(T[1:])            # slice a tuple

T2 = ('Bob', ('dev', 'mgr'))

print(len(T))

T3 = T1 + T2

print(T1 + T2)

if 'Bob' in T2:
    print("Found in Tuple")
else:
    print("Not found in Tuple")

T = ('cc', 'aa', 'dd', 'bb')

tmp = list(T)
tmp.sort()

print(tmp)

T = tuple(tmp)

print(T)

sortedT = sorted(T)

print(sortedT)

T = (1, 2, 3, 4, 5)

L = [x + 20 for x in T]             # convert a tuple to list using list comprehension

print(L)

T = (1, [2, 3], 4)

T[1][0] = 'spam'                    # tuples are immutable but their object data is mutable

print(T)

L = ['grail']

L.append(L)                         # Python prints a [...] whenever it detects a cycle in the object, rather than getting stuck in an infinite loop

print(L)

