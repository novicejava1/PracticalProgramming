#!/usr/bin/env python

import decimal

print(decimal.Decimal(1.23))
print(decimal.Decimal('1.23'))

print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))
print(0.1 + 0.1 + 0.1 - 0.3)

print(decimal.Decimal('0.1') + decimal.Decimal('0.165') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))

print(decimal.Decimal(1) / decimal.Decimal(7))

decimal.getcontext().prec = 4

print(decimal.Decimal(1) / decimal.Decimal(7))

