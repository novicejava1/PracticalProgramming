#!/usr/bin/env python

import time
import sys

print("*" * 60)
print("\tStack Services India - Hiring\t")
print("*" * 60)


data = [{'BU': 'Health Solutions', 'Role': 'UI Developer', 'Exp': '2+ years'},
        {'BU': 'Insurance Solutions', 'Role': 'Dot Net Developer', 'Exp': '3+ years'},
        {'BU': 'Financial Solutions', 'Role': 'Senior/Dot Net Developer', 'Exp': '4+ / 5+ years'},
        {'BU': 'Credit Solutions', 'Role': 'RPG Developer', 'Exp': '4+ years'},
        {'Contact': 'novicejava1', 'Message': 'Message on Linkedin with your resume'}
        ]

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

for each in data:
    if 'Contact' in each:
        print("\n")
        print("Contact  : {}".format(each['Contact']))
        print("Message  : ", end='')
        delay_print(each['Message'])        
    else:
        print("\n")
        print("BU       : {}".format(each['BU']))
        print("Exp      : {}".format(each['Exp']))
        print("Role     : ", end='')
        delay_print(each['Role'])

print("\n")
print("All openings all for XYZ Location")
print("\n")
