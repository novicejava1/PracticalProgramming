#!/usr/bin/env python

from collections import namedtuple

Rec = namedtuple('Rec', ['name', 'age', 'jobs'])        # Make a generated class
bob = Rec('Bob', age=40.5, jobs=['dev', 'mgr'])         # named tuples are a tuple/class/dictionary hybrid

print(bob)
print(list(bob))            # convert to a list

print(bob)
O = bob._asdict()           # convert a tuple to a dict
print(O)

print(O['jobs'][1])         # named tuples build new classes that extend the tuple type, inserting a property accessor method for each named field that maps the name to its position

bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
job, name, age = bob.values()

print(job, name, age)

for x in bob: print(bob[x])

for x in bob.values(): print(x)
