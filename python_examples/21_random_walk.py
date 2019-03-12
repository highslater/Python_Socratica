#!/usr/bin/env python3.7

"""21_random_walk.py.

Nineteenth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import random


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_21.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#21_random_walk.py RUN / START")


def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0

    for i in range(n):
        step = random.choice(list("NSEW"))

        if step == "N":
            y += 1
        elif step == "S":
            y -= 1
        elif step == "E":
            x += 1
        else:
            x -= 1

    return (x, y)


def random_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    x, y = 0, 0

    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

        x += dx
        y += dy

    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home = ", abs(walk[0] + abs(walk[1])))

print('\n', "*" * 40, "\n")
for i in range(25):
    walk = random_walk_2(10)
    print("", walk, "\t Distance from home = ", abs(walk[0] + abs(walk[1])))
print('\n', "*" * 40, "\n")


number_of_walks = 10000
p = 1

for walk_length in range(1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    if no_transport_percentage >= .50 and no_transport_percentage <= p:
        (p, w) = (no_transport_percentage, walk_length)

    print("Walk size =", walk_length,
          "\t: percent = ", round(100 * no_transport_percentage, 2))
print("\n", "Walk size =", w, "\t: percent = ", round(p * 100, 2))
