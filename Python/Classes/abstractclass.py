#!/usr/bin/env python

from abc import ABCMeta, abstractmethod

class Super(metaclass = ABCMeta):                   # defining an Abstract class
    
    def delegate(self):
        self.action()
    
    @abstractmethod                                 # defining an Abstract method in abstract class
    def action(self):                               
        pass

class Sub(Super):
    def action(self):
        print("Spam!!!")

#X = Super()                                         # TypeError: Can't instantiate abstract class Super with abstract method action
X = Sub()
X.delegate()