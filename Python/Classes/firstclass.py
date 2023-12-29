#!/usr/bin/env python

class FirstClass:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

I1 = FirstClass()
I1.setdata("Python")
I1.display()