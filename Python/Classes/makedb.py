#!/usr/bin/env python

from person import Person
from manager import goodManager

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = goodManager('Tom Jones', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()