#!/usr/bin/env python3.7

"""11b_If_Then_Else.py.

Eleventh Program of the Socratica Sexy Hologram Human/Computer Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

N_input = input("Please enter an integer: ")
number = int(N_input)

if number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")
