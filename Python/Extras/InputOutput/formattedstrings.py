import math

year = 2016
event = "Referendum"

# f-strings
print(f'Result of the {year} {event}')
print("Result of the {} {}".format(year, event))

# formatting directives
yes_votes = 42_572_654
no_votes = 43_132_495
print(yes_votes)
print(no_votes)
percentage = yes_votes / (yes_votes + no_votes)
print( "{:-9} YES votes {:2.8%}".format(yes_votes, percentage) )

print(f'{math.pi :.5f}')
print(f'{math.pi}')

# formatting table data
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} {phone:10d}')

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; ' 'Dcab: {0[Dcab]:d}'.format(table))
