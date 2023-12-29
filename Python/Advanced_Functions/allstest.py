from alls import *

print(a)
# print(b)                              # imports only variables list in __all__ list. Load __all__ names only
print(_c)
# print(_d)
print("-" * 100)


from alls import a, b, _c, _d               # other types of import get all names
print(a)
print(b)
print(_c)
print(_d)


import alls                                 # other types of import get all names
print(a)
print("-" * 100)
print(alls.a, alls.b, alls._c, alls._d)