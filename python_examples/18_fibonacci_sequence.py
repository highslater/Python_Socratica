#!/usr/bin/env python3.7

"""18_fibonacci_sequence.py.

Eighteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
from functools import lru_cache


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_18.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

logger.info("#18_fibonacci_sequence.py RUN / START")


def fibonacci(n):
    """Docstring."""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci_cache = {}


def fibonacci_c(n):
    """Docstring."""
    # If there is a value cached, return it.
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci_c(n - 1) + fibonacci_c(n - 2)
    # ache the value and return it
    fibonacci_cache[n] = value

    return value


@lru_cache(maxsize=1000)
def fibonacci_lru(n):
    """Docstring."""
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("Don't Panic! n must be a positive integer.")
    if n < 1:
        raise ValueError("Don't Panic! n must be a positive integer.")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)

"""
for n in range(1, 11):
    print(n, ":", fibonacci(n),)

for n in range(1, 1001):
    print(n, ":", fibonacci_c(n),)
"""
for n in range(1, 51):
    print(n, ":", fibonacci_lru(n), fibonacci_lru(n + 1) / fibonacci_lru(n))
