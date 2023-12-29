#!/usr/bin/env python

S = 'xxxxSPAMxxxxSPAMxxxx'

T = S.replace('SPAM', 'EGGS')

print(T)

T2 = S.replace('SPAM', 'EGGS', 1)           # replace only the first occurance of string

print(T2)

S = 'Spammy'
L = list(S)

print(L)

L[3] = 'b'

print(L)

L2 = ''.join(L)
print(L2)

L2 = '-'.join(L)
print(L2)

line = 'aaa bbb ccc'
cols = line.split(' ')

print(cols)

line = 'aaa,bbb,ccc'
cols = line.split(',')

print(cols)

line = " The knights who say Ni!\n "

print(line.strip())

line = " The knights who say Ni!\n "

print(line.rstrip())

line = " The knights who say Ni!\n "

print(line.lstrip())

line = "This is a alphabetic sentence without any numbers"

print(line.isalpha())

line = "PythonRocks"

print(line.isalpha())

line = "Python123Rocks"

print(line.isalpha())
print(line.isalnum())

print(line.upper())

print('That is %d %s bird!' % (1, 'dead'))      # format expression

exclamation = 'Ni'
print('The knights who say %s!' % exclamation)      # string substitution

print('%d %s %g you' % (1, 'spam', 4.0))        # type specific substitution

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})     # dict based formatting expression 

reply = """
        Greetings...
        Hello %(name)s!
        Your age is %(age)s
        """

values = {'name': 'Bob', 'age': 40}
print(reply % values)

template = '{0}, {1} and {2}'
print(template.format('spam', 'ham', 'eggs'))       # formatting methods by position

template = '{motto}, {pork} and {food}'             # formatting methods by dict keyword
print(template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'                # formatting methods by position and dict keyword
print(template.format('ham', motto='spam', food='eggs'))

template = '{}, {} and {}'                          # formatting methods by relative position
print(template.format('spam', 'ham', 'eggs'))