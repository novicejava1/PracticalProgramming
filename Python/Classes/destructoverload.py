#!/usr/bin/env python

class Life:

    def __init__(self, name='unknown') -> None:
        self.name = name
        print('Hello : ' + name)

    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye ' + self.name)

brian = Life('Brian')

brian.live()