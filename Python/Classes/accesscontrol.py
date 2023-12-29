#!/usr/bin/env python

class AccessControl:

    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
        else:
            raise AttributeError(attr + ' not allowed')


X = AccessControl()

X.age = 40
# X.name = "Bob"                          # AttributeError: name not allowed