#!/usr/bin/env python

import sys

x = 42
x = 'shrubbery'

y = 'Lecture'

print(sys.getrefcount(42))                      # provides the number of references to cached objects in memory
print(sys.getrefcount("Lecture"))               # provides the number of references to cached objects in memory


