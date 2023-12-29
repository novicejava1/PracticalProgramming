#!/usr/bin/env python

import classtree

class Emp:
    pass

class Person(Emp):
    pass

bob = Person()

classtree.instancetree(bob)