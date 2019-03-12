#!/usr/bin/env python3.7

"""22_List_Comprehensions.py.

Twenty-Second Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import random


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_22.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#22_List_Comprehensions.py RUN / START")

numbers = [i for i in range(0, 11)]
evens1 = [i for i in range(0, 11) if i % 2 == 0]
odds1 = [i for i in range(1, 11) if i % 2 == 1]
evens2 = [i for i in range(-10, 11) if i % 2 == 0 and i < 0]
odds2 = [i for i in range(-10, 11) if i % 2 == 1]
no_zero1 = [i for i in evens1 + odds1 if i != 0]
no_zero2 = [i for i in evens2 + odds2]
no_zero1.sort()
no_zero2.sort()
a_to_c = list('abc')
d_to_f = list('def')
a_to_f = [i for i in a_to_c + d_to_f]

a_c_Cartesian_Product_d_f = [(x, y) for x in a_to_c for y in d_to_f]


a = [[1, 3, 5]]
b = [[2, 4, 6]]
c = a + b
ab = [[x[i] for x in c] for i in range(3)]
print(ab)


squares = [i ** 2 for i in range(1, 101)]
e5 = [i ** 2 % 5 for i in range(1, 101)]
e11 = [i ** 2 % 11 for i in range(1, 101)]
'''
        p_remainders = [x**2%p for x in range(0, p)]
        len(p_remainders = p+1/2)

'''
v = [1, 2, 3, 4]
v4 = [4 * x for x in v]
c = [1, 3, 5, 7]
p = [2, 4, 6, 8]
cp = [(x, y) for x in c for y in p]

print(numbers)
print("*" * 90)
print(evens1)
print("*" * 90)
print(odds1)
print("*" * 90)
print(evens2)
print("*" * 90)
print(odds2)
print("*" * 90)
print(no_zero1)
print("*" * 90)
print(no_zero2)
print("*" * 90)
print(a_to_c)
print("*" * 90)
print(d_to_f)
print("*" * 90)
print(a_to_f)
print("*" * 90)
print(a_c_Cartesian_Product_d_f)
print("*" * 90)
print(squares)
print("*" * 90)
print(e5)
print("*" * 90)
print(e11)
print("*" * 90)
print(v)
print("*" * 90)
print(v4)
print("*" * 90)
print(c)
print("*" * 90)
print(p)
print("*" * 90)
print(cp)
print("*" * 90)


num = list("23456789")
face = list("TJQKA")
suit = list("HDCS")
cards = [c for c in num + face]
deck = [[c, s] for c in cards for s in suit]
d = deck.copy()
random.shuffle(d)
e = deck.copy()
random.shuffle(e)

hand1 = [d.pop() for i in range(5)]
hand2 = [d.pop() for i in range(5)]
hand3 = [d.pop() for i in range(5)]
hand4 = [d.pop() for i in range(5)]
hand5 = [d.pop() for i in range(5)]
hand6 = [d.pop() for i in range(5)]

print()
print(d, len(d))
print()
print("", "Hand 1 = ", hand1)
print("", "Hand 2 = ", hand2)
print("", "Hand 3 = ", hand3)
print("", "Hand 4 = ", hand4)
print("", "Hand 5 = ", hand5)
print("", "Hand 6 = ", hand6)
print()

for i in range(3):
    hand1.pop()
    hand1.insert(0, d.pop())

for i in range(3):
    hand2.pop()
    hand2.insert(0, d.pop())

for i in range(3):
    hand3.pop()
    hand3.insert(0, d.pop())

for i in range(3):
    hand4.pop()
    hand4.insert(0, d.pop())

for i in range(3):
    hand5.pop()
    hand5.insert(0, d.pop())

for i in range(3):
    hand6.pop()
    hand6.insert(0, d.pop())

print(d, len(d))
print()
print("", "Hand 1 = ", hand1)
print("", "Hand 2 = ", hand2)
print("", "Hand 3 = ", hand3)
print("", "Hand 4 = ", hand4)
print("", "Hand 5 = ", hand5)
print("", "Hand 6 = ", hand6)


a = [[1, 2, 3]]
b = [list("ABC")]
c = a + b
ab = [[x[i] for x in c] for i in range(3)]
print()
print("", " * A * =", a, " * B * =", b, " * C * =", c, " * AB * =", ab)
