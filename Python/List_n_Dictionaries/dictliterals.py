D = {}

print (D)

D = {'name': 'Bob', 'age': 40}

print(D)

E = {'cto': D}

print(E)

D = dict(name='Bob', age=40)

print(D)

D = dict([('name', 'Bob'), ('age', 40)])

print(D)

keylist = ['name', 'age']
valuelist = ['Torry', 54]

D = dict(zip(keylist, valuelist))

print(D)

print(D['name'])
print(D['age'])

D['class'] = 'First Class'

print(D)

print(list(D.keys()))
print(list(D.values()))

print(D.get('surnam', 'na'))

print(len(D))

D = {'eggs': 3, 'spam': 2, 'ham': 1}
D['ham'] = ['grill', 'bake', 'fry']

print(D)

del D['eggs']

print(D)

D = {'spam': 2, 'ham': 1, 'eggs': 3}

print(type(D.values()))
print(list(D.values()))

print(list(D.items()))

print(D.get('toast', 88))

D = {'eggs': 3, 'spam': 2, 'ham': 1}
D2 = {'toast':4, 'muffin':5}

D.update(D2)

print(D)

print(D.pop('toast'))

Matrix = {}

Matrix[(2, 3, 4)] = 88                  # three dimensional coordinates

Matrix[(7, 8, 9)] = 99

print(Matrix)

if (2, 3, 4) in Matrix:
    print(Matrix[(2, 3, 4)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 4)])
except KeyError:
    print(0)

Matrix.get((2, 3, 4), 0)