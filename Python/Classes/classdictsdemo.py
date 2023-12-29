#!/usr/bin/env python

class Super():
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'


X = Sub()
print(X.__dict__)                               # Instance namespace dict

print(X.__class__)                              # Class of instance

print(Sub.__bases__)                            # Superclasses of class

print(Super.__bases__)

X.hello()

print(X.__dict__)

X.hola()

print(X.__dict__)

Y = Sub()

print(Sub.__dict__.keys())

print(Super.__dict__.keys())