#!/usr/bin/env python3.7

"""07_Python_Numbers.py.

Seventh Program of the Socratica Sexy Robot Python Series.
"""
x = 28
y = 28.0
z = 3.14
c = complex(1.732)
d = 1.732 + 0j

print("x = ", x, type(x))
print("y = ", y, type(y))
print("float(x) = ", float(x), type(float(x)))
print("int(y) = ", int(y), type(int(y)))
print("z = ", z, type(z))
print("int(z) = ", int(z), type(int(z)))
print("c = ", c, type(c))
print("d = ", d, type(d))

a = 2
b = 6.0
c = 12 + 0j

print("a + b = ", a + b, type(a + b))
print("b - a = ", b - a, type(b - a))
print("a * 7 = ", a * 7, type(a * 7))
print("c / b = ", c / b, type(c / b))
print("16 / 5 = ", 16 / 5, type(16 / 5))
print("20 / 5 = ", 20 / 5, type(20 / 5))
print("16 // 5 = ", 16 // 5, type(16 // 5))
print("16 % 5 = ", 16 % 5, type(16 % 5))
print("16 divided by five is " + str(16 // 5) +
      " with a remainder of " + str(16 % 5))
