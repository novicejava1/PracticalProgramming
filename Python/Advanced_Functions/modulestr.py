#!/usr/bin/env python

modname = 'string'
exec('import ' + modname)               # Run a string of code
print(string)                           # Imported in this namespace

modname = 'string'
string = __import__(modname)            # compile module using the __import__ built-in. direct calls to import by name string
print(string)

import importlib
modname = 'string'
string = importlib.import_module(modname)       # direct calls to import by name string
print(string)