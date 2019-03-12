#!/usr/bin/env python3.7

"""19_random_module.py.

Nineteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import random


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_22.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#22_List_Comprehensions.py RUN / START")
"""
squares = [i ** 2 for i in range(1, 101)]
e5 = [i ** 2 % 5 for i in range(1, 101)]
print(squares)
print(e5)
"""

num = list("23456789")
face = list("TJQKA")
suit = list("HDCS")
cards = [c for c in num + face]
deck = [[c, s] for c in cards for s in suit]
d = deck.copy()
random.shuffle(d)
e = deck.copy()
random.shuffle(e)

"""
print(num)
print(face)
print(suit)
print(cards)
print(deck)
"""

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
