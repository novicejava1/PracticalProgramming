#!/usr/bin/env python

def sumtree(L):                                 # Breadth-first, explicit queue. FIFO queue
    total = 0
    items = list(L)
    print(items)
    while items:
        front = items.pop(0)
        print(front)
        if not isinstance(front, list):
            total = total + front
        else:
            print("Before extend")
            print(items)
            items.extend(front)
            print("After extend")
            print(items)
    return total

L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))