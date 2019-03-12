#!/usr/bin/env python3.7

"""14_Lists.py.

Fourteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""

from platform import python_version
from sys import hexversion

print("The Python Version is:", python_version(), " #" + str((hexversion)))

example = list([128, True, "Alpha", 1.732, [64, False]])
example2 = list('abcdef')
example3 = list('12345')
primes = [2, 3, 5, 7, 11, 13]
rolls = [4, 7, 2, 7, 12, 4, 7]
rolls2 = list('4727' '47')  # How to do 12 ?
rolls2.insert(4, '12')

numbers = [1, 2, 3]
letters = list('abc')
phrases = [' easy as ']
phrases2 = [' doe ray me ']

print(example)
print(example2)
print(example3)
print(primes)

primes.append(17)
primes.append(19)
print(primes)

for i in range(len(primes)):
    # if i == len(primes) - 1:
    if primes[i] == primes[-1]:
        print(primes[i], end=" |\n")
    else:
        print(primes[i], end=" * ")
print(primes[2:5])
print(primes[0:6])

print(rolls2)

print(letters + phrases + numbers + phrases2)
forward = letters + phrases + numbers + phrases2
print(forward)

print(rolls)

x = rolls
print(x, x.count(7), x.index(2), x.index(4), x.index(7), x.index(12))

x.reverse()
print(x, x.count(7), x.index(2), x.index(4), x.index(7), x.index(12))

x.sort()
print(x, x.count(7), x.index(2), x.index(4), x.index(7), x.index(12))

x.sort(reverse=True)
print(x, x.count(7), x.index(2), x.index(4), x.index(7), x.index(12))
