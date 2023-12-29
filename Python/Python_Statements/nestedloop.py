#!/usr/bin/env python

while True:
    reply = input("Enter text: ")
    if reply == 'stop' : break
    try:
        num = int(reply)
    except:
        print("Bad!" * 8)
    else:
        if num < 20:
            print("Low")
        else:
            print(num ** 2)
print("Bye!")