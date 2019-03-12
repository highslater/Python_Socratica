#!/usr/bin/env python3.7

"""16_Tuples.py.

Sixteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""


from platform import python_version
from sys import hexversion, getsizeof
from timeit import timeit

print("The Python Version is:", python_version(), " #" + str((hexversion)))

prime_numbers = [2, 3, 5, 7, 11, 13, 17]
perfect_squares = (1, 4, 9, 16, 25, 36)

print("# Primes = ", len(prime_numbers))
print("# Squares = ", len(perfect_squares))

for x in (prime_numbers, perfect_squares):
    for i in x:
        if x == prime_numbers:
            print("Prime: ", i)
        else:
            print("Square: ", i)
print()


def dir_list(t, obj):
    """Docstring."""
    print("", t, "\n", "-" * 88)
    for m in (dir(obj)):
        if m.startswith("_"):
            continue
        elif m.startswith("cou"):
            print("*", str(m).swapcase(), end=" *,  ")
        elif m.startswith("ind"):
            print("*", str(m).swapcase(), end=" *,  ")
        else:
            print("", str(m), end=",  ")
    print("\n\n")

dir_list("List Methods", prime_numbers)
dir_list("Tuple Methods", perfect_squares)

list_eg = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f', 'g',
           False, True, 3.14159]
tuple_eg = (1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 'd', 'e', 'f', 'g',
            False, True, 3.14159)

print("List Size = ", getsizeof(list_eg))
print("Tuple Size = ", getsizeof(tuple_eg))

list_test = timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print("List Time:", list_test)
print("Tuple Time:", tuple_test)
print("It takes ", round(list_test / tuple_test),
      "Times as long to make a list")

empty_tuple = ()
test1 = ('a',)
test2 = ('a', 'b')
test3 = ('a', 'b', 'c')

print(empty_tuple)
print(test1)
print(test2)
print(test3)

test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3

print(test1)
print(test2)
print(test3)

survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
python = survey[2]

print("Age =", age)
print("Country =", country)
print("Python =", python)

survey2 = (21, "Switzerland", False)
age, country, python = survey2

print("Age =", age)
print("Country =", country)
print("Python =", python)

country = ("Australia")
print(country)

country = ("Australia",)
print(country)


'''
a, b, c = (1, 2, 3, 4)

Traceback (most recent call last):
  File "./16_Tuples.py", line 106, in <module>
    a, b, c = (1, 2, 3, 4)
ValueError: too many values to unpack (expected 3)

x, y, z = (1, 2)

Traceback (most recent call last):
  File "./16_Tuples.py", line 115, in <module>
    x, y, z = (1, 2)
ValueError: not enough values to unpack (expected 3, got 2)
'''
