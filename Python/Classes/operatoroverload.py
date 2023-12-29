#!/usr/bin/env python

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

class ThirdClass(SecondClass):
    def __init__(self, value) -> None:
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self) -> str:
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):
        self.data *= other


I1 = FirstClass()
I1.setdata("Python")
I1.display()

I2 = SecondClass()
I2.setdata("43")
I2.display()

a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
print(b)

a.mul(3)
print(a)