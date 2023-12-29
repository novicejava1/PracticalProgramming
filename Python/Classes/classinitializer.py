#!/usr/bin/env python

class C2:
    def setlang(self, language):
        self.language = language

class C3:
    def setregion(self, region):
        self.region = region

class C1(C2, C3):
    def __init__(self, who) -> None:
        self.name = who


I1 = C1("Bob")
I2 = C1("Adam")

print(I1.name)
print(I2.name)
