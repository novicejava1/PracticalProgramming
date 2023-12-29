#!/usr/bin/env python
import decimal
import fractions

int_a = 1234
int_b = 999999999999

print("Integer Literals : ", type(int_a), type(int_b))
print("Integer Literals : ", int_a, int_b)

float_a = 1.23
float_b = 4.0e+210
float_c = 4E210

print("Floating point Literals : ", type(float_a), type(float_b), type(float_c))
print("Floating point Literals : ", float_a, float_b, float_c)

oct_a = 0o177
hex_a = 0x9ff
bin_a = 0b101010

oct_b = oct(25)
hex_b = hex(25)
bin_b = bin(25)

print("Octal, Hex and Binary Literals : ",type(oct_a), type(hex_a), type(bin_a))
print("Octal, Hex and Binary Literals : ",oct_a, hex_a, bin_a)

print("Octal, Hex and Binary Literals : ",type(oct_b), type(hex_b), type(bin_b))
print("Octal, Hex and Binary Literals : ",oct_b, hex_b, bin_b)

complex_a = 2.5j
complex_b = 3 + 4.5j
complex_c = complex(4.5, 2.1)

print("Complex number Literals : ", type(complex_a), type(complex_b), type(complex_c))
print("Complex number Literals : ", complex_a, complex_b, complex_c)

set_old_style = set('Python_Set')
set_dict_form = {1, 2, 3, 4}

print("Set Literals : ", type(set_old_style), type(set_dict_form))
print("Set Literals : ", set_old_style, set_dict_form)

decimal_a = decimal.Decimal('2.5')

print("Decimal Literal : ", type(decimal_a))
print("Decimal Literal : ", decimal_a)

fraction_a = fractions.Fraction(1,3)

print("Fractional Literal : ", type(fraction_a))
print("Fractional Literal : ", fraction_a)

bool_a = True
bool_b = False

print("Boolean Literals : ", type(bool_a), type(bool_b))
print("Boolean Literals : ", bool_a, bool_b)