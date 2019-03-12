#!/usr/bin/env python3.7

"""11c_If_Then_Else.py.

Eleventh Program of the Socratica Sexy Hologram Human/Computer Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

print(abs(a + b + c))

if (a + b + c) != (abs(a) + abs(b) + abs(c)):
    print("This is NOT a valid triangle")

else:

    if a != b and a != c and b != c:
        print("This is a SCALENE triangle.")
    elif a == b and b == c and a == c:
        print("This is an EQUILATERAL triangle")
    else:
        print("This is a ISOCELES triangle")
