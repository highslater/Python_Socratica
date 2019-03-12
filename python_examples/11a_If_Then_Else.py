#!/usr/bin/env python3.7

"""11a_If_Then_Else.py.

Eleventh Program of the Socratica Sexy Hologram Human/Computer Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

input = input("Please enter a test string: ")

if len(input) < 6:
    print("Your string is too short")
    print("Please enter a string with at least six characters.")
