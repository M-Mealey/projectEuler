"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math
from local_helpers import is_prime

def largest_prime_factor(x):
    largest_factor = 0
    for i in range(2, int(math.sqrt(x))):
        if x%i == 0 and is_prime(i):
            largest_factor = i
    if largest_factor == 0:
        largest_factor = x
    return largest_factor

print(largest_prime_factor(600851475143))
