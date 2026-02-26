"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

import math


def find_next_factor(x):
    if not isinstance(x, int) or x <= 1:
        return -1
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return i
    return x


def find_prime_factors(x):
    factors = set()
    f = find_next_factor(x)
    while f > 0:
        factors.add(f)
        x = int(x/f)
        f = find_next_factor(x)
    return factors


def euler_problem_47():
    counter = 0
    for i in range(1, 1000000):
        if len(find_prime_factors(i)) == 4:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            print(i - 3)
            break


if __name__ == "__main__":
    euler_problem_47()
