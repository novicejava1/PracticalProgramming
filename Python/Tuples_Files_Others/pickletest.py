#!/usr/bin/env python

import pickle

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')

pickle.dump(D, F)                           # pickle stores and restores data persisting the object type
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E)
F.close()