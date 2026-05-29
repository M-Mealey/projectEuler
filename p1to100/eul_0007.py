"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve


def solve():
    """ solve problem 7 """
    max_number = 1000000
    prime_list = prime_sieve(max_number)
    return prime_list[10000]


if __name__ == "__main__":
    print(solve())
