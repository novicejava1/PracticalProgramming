#!/usr/bin/env python

import json

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)

print(rec)

F = open('testjson.txt', 'w')
S = json.dump(rec, F, indent=4)
F.close()

F = open('testjson.txt', 'r')
print(F.read())
F.close()

P = json.load(open('testjson.txt'))
print(P)