#!/usr/bin/env python3.7

"""19_random_module.py.

Nineteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import random


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_19.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#19_random_module.py RUN / START")

print("\n", "*" * 25, "\n")
for n in range(10):
    print("", random.random())


def my_random():
    """Return a random number between 3 and 7."""
    return 4 * random.random() + 3


print("\n", "*" * 25, "\n")
for n in range(10):
    print("", my_random())

print("\n", "*" * 25, "\n")
for n in range(10):
    print("", random.uniform(3, 7))

print("\n", "*" * 25, "\n")
for n in range(10):
    print("", random.normalvariate(5, .2))

print("\n", "*" * 25, "\n")
for n in range(20):
    print("", random.randint(1, 6), end=", ")
print()

outcomes = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
print("\n", "*" * 25, "\n")
for n in range(20):
    print("", random.choice(outcomes), end=", ")
print()

print("\n", "*" * 25, "\n")
