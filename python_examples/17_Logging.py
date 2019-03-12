#!/usr/bin/env python3.7

"""17_Logging.py.

Seventeenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import math

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_17.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

'''
print(logger.level)
logger.debug("17_Logging.py. RUN TEST")
logger.info("17_Logging.py. RUN TEST")
logger.warning("17_Logging.py. RUN TEST")
logger.error("17_Logging.py. RUN TEST")
logger.critical("17_Logging.py. RUN TEST")
'''
logger.info("# 17_Logging.py. RUN / START")


def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("# quadratic_formula({0}, {1},{2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b ** 2 - 4 * a * c
    logger.debug("# Discriminant computed as: ({0})".format(disc))

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root_1 = (-b + math.sqrt(disc)) / (2 * a)
    root_2 = (b + math.sqrt(disc)) / (2 * a)
    logger.debug("# Roots computed as: ({0}, {1})".format(root_1, root_2))

    # return the two roots as a tuple
    logger.debug("# return the two roots as a tuple")
    t = (root_1, root_2)
    logger.debug("# Tuple returned as: {0}".format(t))

    return t

roots = quadratic_formula(1, 0, -4)
print(roots)

roots = quadratic_formula(1, 0, 1)
print(roots)
