#!/usr/bin/env python

from person import Person

class BadManager(Person):

    def __init__(self, name, pay) -> None:
        Person.__init__(self, name, 'mgr', pay)

    def giveRise(self, percent, bonus=.10):                         # Bad way of augmenting methods
        self.pay = int(self.pay * (1 + percent + bonus))

class goodManager(Person):

    def __init__(self, name, pay) -> None:
        Person.__init__(self, name, 'mgr', pay)

    def giveRise(self, percent, bonus=.10):
        # return super().giveRise(percent + bonus)
        return Person.giveRise(self, percent + bonus)

if __name__ == '__main__':


    sue = Person('Sue Jones', job='dev', pay=100000)

    teddy = BadManager('Teddy Jones', pay=100000)
    teddy.giveRise(10)
    print(teddy)

    dude = goodManager('Dude Lake', pay=100000)
    dude.giveRise(10)
    print(dude)

    tom = goodManager('Tom Jones', 50000)
    tom.giveRise(.10)
    print(tom.lastName())
    print(tom)

    for obj in (sue, teddy, dude, tom):
        obj.giveRise(.10)
        print(obj)