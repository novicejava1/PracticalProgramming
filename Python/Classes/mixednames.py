#!/usr/bin/env python

class MixedNames:
    
    data = 'spam'

    def __init__(self, value) -> None:
        self.data = value
    
    def display(self):
        print(self.data, MixedNames.data)


x = MixedNames('changed')
y = MixedNames(2)

print(x.data)
print(y.data)
print(MixedNames.data)

x.display()
y.display()