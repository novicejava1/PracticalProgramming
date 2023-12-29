#!/usr/bin/env python

import json

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)

print(rec)

S = json.dumps(rec)
print(S)

O = json.loads(S)
print(O)

if O == rec:
    print("Reload successfull")
else:
    print("Reload failed")