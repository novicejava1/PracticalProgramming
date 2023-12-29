import sys
import dir1                             # __init__.py is automatically executed even though its not imported
import dir1.dir2                        # __init__.py is automatically executed even though its not imported
import dir1.dir2.mod

print(sys.path)

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

from dir1.dir2 import mod
from dir1.dir2 import mod as m


print(mod.z)
print(m.z)