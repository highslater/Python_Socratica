#!/usr/bin/env python3.7

"""13_Sets.py.

Thirteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

example = set()
print(dir(example))

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example, len(example))

example.add(42)
print(example, len(example))

example.remove(42)
print(example, len(example))

example.add(50)
print(example, len(example))

example.discard(50)
print(example, len(example))

example2 = {28, True, 2.71821, "Helium"}
print(example2, len(example2))

example2.clear()
print(example2, len(example2))

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds, evens)
print(odds.union(evens))
print(evens.union(odds))
print(odds, evens)

print(odds.intersection(primes))
print(evens.intersection(primes))
print(evens.intersection(odds))
print(primes.union(composites))

print(2 in primes)
print(6 in odds)
print(9 not in evens)

x = set([1, 2, 3, 4, 5])
y = set([1, 2, 3])

print(x.difference(y))
print(y.issubset(x))
print(x.issuperset(y))
