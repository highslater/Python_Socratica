#!/usr/bin/env python3.7

"""26_Lambda_Expressions.py.

Twenty-Sixth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
from math import sqrt


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_26.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#26_Lambda_Expressions.py RUN / START")

g = lambda x: 3 * x + 1

print('*' * 94, "\n")

for i in range(2, 21, 2):
    print((i, g(i)), end="  ")
print("\n")
print('*' * 94)

full_name = (
    lambda firstname, lastname:
    firstname.strip().title() + " " + lastname.strip().title()
)

print('*' * 94, "\n")
print(full_name("   leonard", "  EULER  "))
print("\n")
print('*' * 94)

a = lambda: "What is your quest?"
b = lambda x: x ** 2 - 4
c = lambda a, b: sqrt(a ** 2 + b ** 2)
d = lambda a, b, c: a ** 2 + b ** 2 == c ** 2  # Test

print('*' * 94, "\n")
print(a())
print(b(2))
print(c(3, 4))
print(d(3, 4, 5))
print(d(3, 4, 6))
print("\n")
print('*' * 94)

jbs = ["Jason Bourne", "Jack Bauer", "Jason Bauer", "Jack Bourne"]

jbs.sort(key=lambda name: name.split(" ")[-1].lower())

print('*' * 94, "\n")
print(jbs)
print("\n")
print('*' * 94)

jbs.sort(key=lambda name: name.split(" ")[0].lower())

print('*' * 94, "\n")
print(jbs)
print("\n")
print('*' * 94)
print("""
        Alphabetize both first and last.
        [""Jack Bauer", "Jason Bauer", "Jack Bourne", Jason Bourne"]
""")


def build_quadratic_function(a, b, c):
    """Return the function f(x) = ax^2 + bx = c ."""
    return lambda x: a * x ** 2 + b * x + c

f = build_quadratic_function(2, 3, -5)

print('*' * 94, "\n")
print(f(0))
print(f(1))
print(f(2))

print(build_quadratic_function(3, 0, 1)(2))

print("\n")
print('*' * 94)
