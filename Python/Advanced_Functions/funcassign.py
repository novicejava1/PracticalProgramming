#!/usr/bin/env python

def echo(message):
    print(message)

def indirect(func, arg):
    func(arg)                                   # Call the passed-in object by adding ()

x = echo
x("Hello Python")
echo("Hello Django")

indirect(echo, "Argument Call!!")               # Pass the function to another function
