#!/usr/bin/env python

X = 1

def nester():
    X = 2
    print(X)

    class C:
        X = 3
        print(X)

        def method1(self):
            print(X)                # In enclosing def (not 3 in class!): 2
            print(self.X)           # Inherited class local: 3
        
        def method2(self):
            X = 3
            print(X)
            self.X = 5
            print(self.X)
        
    I = C()
    I.method1()
    I.method2()

print(X)
nester()
print('-' * 40)