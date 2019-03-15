#!/usr/bin/env python3.7

"""27_Map_Filter_Reduce.py.

Twenty-Seventh Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
from statistics import mean
from functools import reduce

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


temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
         ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
         ("London", 22), ("Beijing", 32)]

c_to_f = lambda data: ([data[0], 9 / 5 * data[1] + 32])
lm = list(map(c_to_f, temps))
print("\n", "*" * 110, "\n")
print("", lm)
print("\n", "*" * 110, "\n")

# ======= Filter Function =======

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
ave = mean(data)
above_ave = list(filter(lambda x: x > ave, data))
below_ave = list(filter(lambda x: x < ave, data))
print("\n", "*" * 110, "\n")
print("ABOVE:\t\t\t", above_ave)
print("BELOW:\t\t\t", below_ave)
print("\n", "*" * 110, "\n")

countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia",
             "", "Ecuador", "", "", "Venezuela"]
c = list(filter(None, countries))
print("\n", "*" * 110, "\n")
print("\t\t", c)
print("\n", "*" * 110, "\n")

# ======= Reduce Function =======

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x * y
md = reduce(multiplier, data)
print("\n", "*" * 110, "\n")
print("\t\t\t", md)
print("\n", "*" * 110, "\n")

product = 1
for x in data:
    product = product * x
print("\n", "*" * 110, "\n")
print("\t\t\t", product)
print("\n", "*" * 110, "\n")
