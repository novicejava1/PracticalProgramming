#!/usr/bin/env python

# multiway branching using if - else

x = 'killer rabbit'
if x == 'roger':
    print("shave and a haircut")
elif x == 'bugs':
    print("what's up doc?")
else:
    print("Run away! Run away!")


# dictionary as multiway branching. Easy to run with exec and eval tools

choice = 'ham'
data = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}
print(data[choice])                         


# getting the default incase of any exception

data = {'spam': 1.25, 'ham': 1.99, 'eggs': 0.99, 'bacon': 1.10}
print(data.get('spam', 'Bad choice, No dict key'))
print(data.get('spam2', 'Bad choice, No dict key'))

