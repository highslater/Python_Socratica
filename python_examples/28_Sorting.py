#!/usr/bin/env python3.7

"""28_Sorting.py.

Twenty-Eighth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_28.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("28_Sorting.py RUN / START")

earth_metals = ["Beryllium", "Magnesium", "Calcium",
                "Strontium", "Barium", "Radium"]

# ====== Sorting ======

print("\n", "*" * 90)
print("\n\t", earth_metals)
print("\n", "*" * 90)

earth_metals.sort()
print("\n", "*" * 90)
print("\n\t", earth_metals)
print("\n", "*" * 90)

earth_metals.sort(reverse=True)
print("\n", "*" * 90)
print("\n\t", earth_metals)
print("\n", "*" * 90)

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.00),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]
# ====== Sorting (name) ======

print("\n", "*" * 32)
for p in planets:
    print("\n", p)
print("\n", "*" * 32)

# ====== Sorting (size) ======

planets.sort(key=lambda planet: planet[1], reverse=True)
print("\n", "*" * 32)
for p in planets:
    print("\n", p)
print("\n", "*" * 32)
# ====== Sorting (density) ======

planets.sort(key=lambda planet: planet[2])
print("\n", "*" * 32)
for p in planets:
    print("\n", p)
print("\n", "*" * 32)

# ====== Sorting (distance ======

planets.sort(key=lambda planet: planet[3])
print("\n", "*" * 32)
for p in planets:
    print("\n", p)
print("\n", "*" * 32)

earth_metals = ["Beryllium", "Magnesium", "Calcium",
                "Strontium", "Barium", "Radium"]

# ====== Sorting a copy with sorted() ======

print("\n", "*" * 90)
print("\n\t", earth_metals)
print("\n", "*" * 90)

sorted_earth_metals = sorted(earth_metals)
print("\n", "*" * 90)
print("\n\t", sorted_earth_metals)
print("\n\t", earth_metals)
print("\n", "*" * 90)

data = (9, 8, 7, 6, 5, 4, 3, 2, 1)
sdata = sorted(data)
print("\n", "*" * 90)
print("\n\t", sdata)
print("\n\t", data)
print("\n", "*" * 90)

a = "Alphabetical"
print("\n", "*" * 90)
print("\n\t", a)
print("\n\t", sorted(a))
print("\n", "*" * 90)
