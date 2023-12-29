#!/usr/bin/env python

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights()
msg = act('robin')
print(msg)
