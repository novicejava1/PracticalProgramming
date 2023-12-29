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
    

class Manager:
    def __init__(self, name, pay) -> None:
        self.person = Person(name, 'mgr', pay)                  # Embed a Person object

    def giveRaise(self, percent, bonus=.10):                    # Intercept and delegate
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):                                # Delegate all other attrs
        return getattr(self.person, attr)                   
    
    def __repr__(self):
        return str(self.person)                                 # Must overload again (in 3.X)
    

if __name__ == '__main__':


    sue = Person('Sue Jones', job='dev', pay=100000)

    teddy = Manager('Teddy Jones', pay=100000)
    teddy.giveRise(10)
    print(teddy)

    dude = Manager('Dude Lake', pay=100000)
    dude.giveRise(.10)
    print(dude)

    tom = Manager('Tom Jones', 50000)
    tom.giveRise(.10)
    # print(tom.lastName())
    print(tom)

    for obj in (sue, teddy, dude, tom):
        obj.giveRise(.10)
        print(obj)