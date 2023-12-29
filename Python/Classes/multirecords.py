#!/usr/bin/env python

class rec: pass

pers1 = rec()
pers2 = rec()

pers1.name = 'Bob'
pers1.age = 35
pers1.jobs = ['dev', 'mgr']

pers2.name = 'Adam'
pers2.age = 40
pers2.jobs = ['dev', 'ops']

print(pers1, pers2)

print(pers1.name, pers1.age, pers1.jobs)
print(pers2.name, pers2.age, pers2.jobs)

