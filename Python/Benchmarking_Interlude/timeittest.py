#!/usr/bin/env python

import timeit


# repeat the opreration 5 times with stmt executing 1000 times and producing 1000 item list on each execution
print(min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5)))          # single statement timing 

print(min(timeit.repeat(number=10000, repeat=3,
      stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1"))                   # multiline statement timing     
    )