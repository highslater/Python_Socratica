#!/usr/bin/env python3.7

"""27_Map_Filter_Reduce.py.

Twenty-Seventh Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging

from my_functions.circles import circle_area
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_27.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("27_Map_Filter_Reduce.py RUN / START")

# ======= Map Function =======

radii = [2, 5, 7.1, 0.3, 10]
areas = []
for r in radii:
    a = round(circle_area(r), 1)
    areas.append(a)

print("\n", "*" * 90, "\n")
print("\t\t\t", areas)
print("\n", "*" * 90, "\n")

l = list(map(circle_area, radii))
print("\n", "*" * 90, "\n")
print("\t\t\t", l)
print("\n", "*" * 90, "\n")

ll = list(map(lambda x: round(circle_area(x), 2), radii))
print("\n", "*" * 90, "\n")
print("\t\t\t", ll)
print("\n", "*" * 90, "\n")

lll = lambda y: list(map(lambda x: round(circle_area(x), y), radii))
print("\n", "*" * 90, "\n")
print("\t\t\t", lll(3))
print("\n", "*" * 90, "\n")

llll = lambda y, xs: list(map(lambda x: round(circle_area(x), y), xs))
print("\n", "*" * 110, "\n")
print("", llll(1, [x for x in range(0, 11, 1)]))
print("\n", "*" * 110, "\n")

lllll = lambda y: list(map(
    lambda x: round(circle_area(x), y), [x for x in range(0, 11, 1)]))
print("\n", "*" * 110, "\n")
print("", lllll(2))
print("\n", "*" * 110, "\n")
