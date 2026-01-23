"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math
from local_helpers import is_prime


sum = 17
for i in range(2000000):
    if is_prime(i):
        sum += i
print(sum)
