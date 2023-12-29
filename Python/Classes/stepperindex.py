#!/usr/bin/env python

class StepperIndex:

    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = "Spam"

print(X[1])                                     # Indexing calls __getitem__

for item in X:                                  # for loops call __getitem__
    print(item, end=' ')

print(list(map(str.upper, X)))

print(list(X), tuple(X), ''.join(X))