#!/usr/bin/env python

import time

def timer(func, *args):
    start = time.process_time()
    for i in range(1000):
        func(*args)
    return time.process_time() - start


latency = timer(pow, 2, 1000)
print(latency)

latency = timer(str.upper, 'spam')
print(latency)