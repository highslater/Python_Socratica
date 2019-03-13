#!/usr/bin/env python3.5

"""circles.py.

Thirtieth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
from math import pi


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_1.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("#circles.py RUN / START")


def circle_area(r):
    """Return the area of circle with radius r."""
    if type(r) not in [int, float]:
        raise TypeError("Nope. The RADIUS must be NON-NEGATIVE and REAL")
    if r < 0:
        raise ValueError("Nope. The RADIUS cannot be NEGATIVE")

    return pi * (r ** 2)
