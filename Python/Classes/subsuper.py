#!/usr/bin/env python

class Super():

    def method(self):
        print("In Super.methods")


class Sub(Super):
    def method(self):
        print("Starting sub.method")
        super().method()
        print("ending sub.method")

x = Super()
x.method()

y = Sub()
y.method()