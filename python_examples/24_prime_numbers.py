#!/usr/bin/env python3.5

"""24_prime_numbers.py.

Twenty-Fourth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging
import time
import math
import pid

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_24.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info("#24_prime_numbers.py RUN / START")


def is_prime_v1(n):
    """Docstring."""
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

# ===== Test Function =====
'''
for n in range(1, 50000):
    print("", n, is_prime_v1(n))

'''
# ===== Time Function =====
'''
t0 = time.time()

for n in range(1, 100000):
    is_prime_v1(n)

t1 = time.time()

print("Time Required = ", t1 - t0)
'''
'''
        Time Required =  71.59234523773193

'''


def is_prime_v2(n):
    """Docstring."""
    if n == 1:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

# ===== Test Function =====
'''
for n in range(1, 21):
    print("", n, is_prime_v2(n))
'''
'''
# ===== Time Function =====

t0 = time.time()

for n in range(1, 100000):
    is_prime_v2(n)

t1 = time.time()

print("Time Required = ", t1 - t0)
'''
'''
Time Required =  0.46372342109680176

'''


def is_prime_v3(n):
    """Docstring."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


# ===== Test Function =====
'''
for n in range(1, 21):
    print("", n, is_prime_v3(n))
'''
'''
# ===== Time Function =====

t0 = time.time()

for n in range(1, 10000000):
    is_prime_v3(n)

t1 = time.time()

print("Time Required = ", t1 - t0)
'''
'''
Time Required =  140.9158058166504

'''


def gen_primes(n):
    """Docstring."""
    primes = []
    for i in range(1, n + 1):
        if is_prime_v3(i) is True:
            primes.append(i)
    return primes

# ===== Time Function =====
'''
t0 = time.time()

p = (gen_primes(1000000))

t1 = time.time()


print("Time Required =", round((t1 - t0), 2), "# of Primes =", len(p))
'''
'''
Time Required = 5.55 # of Primes = 78498

'''
'''
# ===== Time Function =====

t0 = time.time()

p = (gen_primes(10000000))

t1 = time.time()

print("Time Required =", round((t1 - t0), 2), "# of Primes =", len(p))
'''

'''
Time Required = 140.38 # of Primes = 664579

'''
'''

# ===== Time Function =====

t0 = time.time()
#100,000,000 One Hundred Million
p = (gen_primes(100000000))

t1 = time.time()

print("Time Required =", round((t1 - t0), 2), "# of Primes =", len(p))

'''
'''
Time Required = 3752.69 # of Primes = 5761455

'''
"""
with pid.PidFile(piddir='/home/j/Programming/Socratica_Python'
                        '/python_examples/PID_files'):
    t0 = time.time()
    p = (gen_primes(100000000))  # 100,000,000 One Hundred Million
    t1 = time.time()

print("Time Required =", round((t1 - t0), 2), "# of Primes =", len(p))
"""

"""
Time Required = 4817.08 # of Primes = 5761455

"""
