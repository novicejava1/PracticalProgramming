#!/usr/bin/env python

movies = {'name': 'Jo Jeeta Wohi Sikandar', 'year': '1990', 'actor': 'Aamir'}

print(movies)

# Get Movie name
print(movies['name'])

# Get Movie year
print(movies['year'])

# Get Movie Actor
print(movies['actor'])

# Add a new key to the dictionary
movies['director'] = 'Yash'

print(movies)

# Create a new dictionary using dict
bob1 = dict(name='bob', job='dev', age=40)

# print bob
print(bob1)

# Crate a new dictionary using zip format example
bob2 = dict(zip(['name', 'job', 'age'], ['Bobby', 'Architect', '32']))

# print bob2
print(bob2)