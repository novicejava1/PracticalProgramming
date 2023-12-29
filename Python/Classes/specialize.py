#!/usr/bin/env python

class Super:
    
    def method(self):                   
        print("In Super.method")                # Default behavior
    def delegate(self):                         
        self.action()                           # Expected to be defined

class Inheritor(Super):                         # Inherit method verbatim
    pass

class Replacer(Super):                          # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super):                          # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()