"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

primes = [2, 3, 5, 7, 11, 13, 17, 19]


def prime_factors(x):
    """ for given x, return prime factors of x between 1 and 20"""
    index = 0
    factors = []
    while x > 1 and index < 8:
        if x % primes[index] == 0:
            factors.append(primes[index])
            x /= primes[index]
        else:
            index += 1
    return factors


def lcm(x):
    """ for list x, find least common multiple of all ints in list"""
    powers = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in x:
        factors = prime_factors(i)
        for n, prime in enumerate(primes):
            powers[n] = max(powers[n], factors.count(prime))
    m = 1
    for n, prime in enumerate(primes):
        m *= (prime**powers[n])
    return m


def solve():
    """ solve problem 5 """
    return lcm(range(20))


if __name__ == "__main__":
    print(solve())
