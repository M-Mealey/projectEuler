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
    powers = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in x:
        factors = prime_factors(i)
        for n in range(len(primes)):
            powers[n] = max(powers[n], factors.count(primes[n]))
    lcm = 1
    for n in range(len(primes)):
        lcm *= (primes[n]**powers[n])
    return lcm


def euler_problem_5():
    print(lcm(range(20)))


if __name__ == "__main__":
    euler_problem_5()
