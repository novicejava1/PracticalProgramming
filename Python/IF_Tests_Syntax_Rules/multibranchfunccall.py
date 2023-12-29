#!/usr/bin/env python

def usage():
    return "Its usage function"

def list():
    return "Its list function"

def getdata():
    return "Its get function"

def setdata():
    return "Its set function"

def default():
    return "Its default function"

branch = {'usage': usage, 'list': list, 'getdata': getdata, 'setdata': setdata}

print(branch['usage'])
print(branch.get('usage', default)())
print(branch.get('list', default)())
print(branch.get('setdata', default)())
print(branch.get('getdata', default)())
print(branch.get('deldata', default)())