#!/usr/bin/env python

def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))

# func(toast=20, ham=40)                      # positional arguments need to be provided
func(14, 12, toast=20, ham=40)