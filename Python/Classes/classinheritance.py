#!/usr/bin/env python

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

I1 = FirstClass()
I1.setdata("Python")
I1.display()

I2 = SecondClass()
I2.setdata("43")
I2.display()