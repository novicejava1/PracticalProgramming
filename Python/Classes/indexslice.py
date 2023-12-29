#!/usr/bin/env python

class Indexer():
    
    data = [5 ,6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

X = Indexer()

print(X[1])
print(X[4])

print(X[2:4])