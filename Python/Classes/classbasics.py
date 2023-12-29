#!/usr/bin/env python

class C2:
    def setlang(self, language):
        self.language = language

class C3:
    def setregion(self, region):
        self.region = region

class C1(C2, C3):
    def setname(self, who):
        self.name = who

I1 = C1()
I2 = C1()

I1.setname("Bob")
I1.setlang("Python")
I1.setregion("Asia")

I2.setname("Adam")
I2.setlang("Django")
I2.setregion("Australia")

print(I1.name)
print(I1.language)
print(I1.region)

print(I2.name)
print(I2.language)
print(I2.region)