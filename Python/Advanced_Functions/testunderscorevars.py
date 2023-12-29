from underscorevars import *                    # Load non _X names only

print(a)
# print(_b)                                       # from * # Load non _X names only
print(c)
# print(_d)
print("-" * 100)
import underscorevars                           # import loads all names

print(underscorevars.a)
print(underscorevars._b)
print(underscorevars.c)
print(underscorevars._d)

