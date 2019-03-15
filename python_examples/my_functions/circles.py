#!/usr/bin/env python3.5

"""circles.py.

Thirtieth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
from math import pi


def circle_area(r):
    """
    Return the area of circle with radius r.

    rounded to 2 places.

    """
    if type(r) not in [int, float]:
        raise TypeError("Don't Panic! but,"
                        "Nope. The RADIUS must be NON-NEGATIVE and REAL")
    if r < 0:
        raise ValueError("Don't Panic! but,"
                         "Nope. The RADIUS cannot be NEGATIVE")

    return (pi * (r ** 2))
