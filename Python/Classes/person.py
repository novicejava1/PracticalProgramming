#!/usr/bin/env python

class Person:
    def __init__(self, name, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    
    def giveRise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

if __name__ == '__main__':                                  # When imported, the file now defines the class, but does not use it
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    #print(bob.name, bob.pay)
    #print(sue.name, sue.pay)

    # print(bob.name.split()[-1])                           # move operations from outside class to class methods
    #sue.pay *= 1.10
    # print('%.2f' % sue.pay)

    print(bob.lastName(), sue.lastName())
    sue.giveRise(10)
    print(bob.name, sue.name)
    print(bob.pay, sue.pay)
    print(bob, sue)