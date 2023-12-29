#!/usr/bin/env python

import timer

print(timer.total(1000, pow, 2, 1000)[0])               # return elapsed time
print(timer.total(1000, pow, 2, 1000)[1])               # returns the result

print(timer.total(1000, pow, 2, 1000))                  # returns both elapase time and result


print(timer.bestof(1000, pow, 2, 1000)[0])
print(timer.bestof(1000, pow, 2, 1000)[1])
print(timer.bestof(1000, pow, 2, 1000))

print(timer.bestof(50, timer.total, 1000, str.upper, 'spam'))
print(timer.bestoftotal(50, 1000, str.upper, 'spam'))

print(min(timer.total(1000, str.upper, 'spam') for i in range(50)))