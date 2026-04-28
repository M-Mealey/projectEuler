"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""
import math
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve


def largest_prime_factor(x):
    """ returns the largest prime factor for a given x """
    prime_set = set(prime_sieve(math.ceil(math.sqrt(x))))
    largest_factor = 0
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0 and i in prime_set:
            largest_factor = i
    if largest_factor == 0:
        largest_factor = x
    return largest_factor


def solve():
    """ solve problem 3 """
    return largest_prime_factor(600851475143)


if __name__ == "__main__":
    print(solve())
