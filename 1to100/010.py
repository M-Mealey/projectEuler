"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math
from local_helpers import prime_sieve


def euler_problem_10():
    primes = prime_sieve(2000000)
    print(sum(primes))


if __name__ == "__main__":
    euler_problem_10()
