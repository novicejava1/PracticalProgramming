#!/usr/bin/env python

a = 3
b = 4

print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(a + 4.0, 2.0 ** b)
# print(c * 2)
print(b / 2 + a)
print(b // 2 + a)
print(b / (2.0 + a))

num = 1 / 3.0

print(num)
print("%e" % num)
print("%4.2f" % num)
print("{0:4.2f}".format(num))

x = 25
y = 33
z = 57

print(x < y)
print(z > x)
print(y < z < x)
print(x == y)
print(x != y)

border_x = 0
border_y = 24
my_place = 15
print(border_x < my_place < border_y)
if border_x < my_place < border_y:
    print("I am within border range")
else:
    print("I am out of border range")