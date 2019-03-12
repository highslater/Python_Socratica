#!/usr/bin/env python3.7

"""09_Booleans.py.

Ninth Program of the Socratica Sexy Hologram Python Series.
"""
from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

a = 3
b = 5
print("a = ", a)
print("b = ", b)
print("a == b is: ", a == b)
print("a != b is: ", a != b)
print("a < b is: ", a < b)
print("a > b is: ", a > b)

print("type(True) is: ", type(True))
print("type(False) is: ", type(False))

print("bool(28) is: ", bool(28))
print("bool(-2.71828) is: ", bool(-2.71828))
print("bool(0) is: ", bool(0))

print('bool("Turing") is: ', bool("Turing"))
print('bool(" ") is: ', bool(" "))
print('bool("") is: ', bool(""))

print("str(True) is: ", str(True), type(str(True)))
print("str(False) is: ", str(False), type(str(False)))

print("int(True) is: ", int(True), type(int(True)))
print("int(False) is: ", int(False), type(int(False)))

print("5 + True is: ", 5 + True, type(5 + True))
print("10 * False is: ", 10 * False, type(10 * False))
