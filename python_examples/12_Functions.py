#!/usr/bin/env python3.7

"""12_Functions.py.

Twelfth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion
import time

print("The Python Version is:", python_version(), " #" + str((hexversion)))


def count(x):
    """Obligatory DocString."""
    for i in range(x, 0, -1):
        print("\r", end=" ", flush=True)
        print(("---" * (i)) + "---", i, end=" ", flush=True)
        time.sleep(.6)

        print("\r", end=" ", flush=True)
        print(("~~~" * (i)) + "~~", " ", end=" ", flush=True)
        time.sleep(.4)

    print("\r", end="  ", flush=True)
    print("  " * x, end="  \n", flush=True)
    time.sleep(.5)
    print("Functions!")


def ping(n):
    """Obligatory DocString."""
    t = ''.join(["*" for i in range(n)])
    s = []

    for i in range(n):
        s.append("!")
    p = "".join(s)
    return p, t


count(15)
time.sleep(0)

# x = ping(10)
# print(x[0])
# print(x[1])
