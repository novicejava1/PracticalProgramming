#!/usr/bin/env python

class Squares:
    
    def __init__(self, start, stop) -> None:
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
    

if __name__ == '__main__':
    for i in Squares(1, 5):                     # for calls iter, which calls __iter__
        print(i, end=' ')                       # Each iteration calls __next__

    X = Squares(1, 5)
    print(tuple(X), tuple(X))                   # Iterator exhausted in second tuple()
    
    X = list(Squares(1, 5))                     # Iterator objects converted to list so they dont exhaust
    print(tuple(X), tuple(X), tuple(X))