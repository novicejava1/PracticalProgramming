#!/usr/bin/env python

class rec:
    pass

rec.name = 'Bob'                        # Just objects with attributes
rec.age = 40

print(rec.name)                         # Like a C struct or a record
print(rec.age)

x = rec()
y = rec()

print(x.name)
print(x.age)

print(y.name)
print(y.age)

x.name = 'changed'

print(rec.name, x.name, y.name)

print(list(rec.__dict__.keys()))                            # class level dict attributes

print(list(name for name in rec.__dict__ if not name.startswith('__')))     # class level dict attributes without __

print(list(x.__dict__.keys()))                              # instance level dict attributes 

print(list(y.__dict__.keys()))                              # instance level dict attributes. Empty because no attributes set at instance level

print(x.name, x.__dict__['name'])                           # Attributes present here are dict keys

print(x.age)                                                # Attributes fetch checks classes too

# print(x.__dict__['age'])                                    # Indexing dict does not do inheritance
