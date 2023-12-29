#!/usr/bin/env python

import sys
import minmax


print(dir(minmax))

print(minmax.__name__)                                      # Qualify object by attribute
print(minmax.__dict__['__name__'])                          # Index namespace dictionary manually
print(sys.modules['minmax'].__name__)                       # Index loaded-modules table manually
print(getattr(minmax, '__name__'))                          # Call built-in fetch function