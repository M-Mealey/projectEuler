"""
Project Euler Problem 72
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d 1,000,000?
"""

# how many fractions don't reduce?
# won't reduce when numerator is relatively prime, so for denominator d
# the number of elements it adds to the set is the number of integers >d that are relatively prime
# aka totient
import math

# Copied from problem 47


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


def calculate_totient(n):
    prime_factors = find_prime_factors(n)
    totient = n
    for p in prime_factors:
        totient *= (1 - 1/p)
    return totient


total = 21
for d in range(9, 1000001):
    total += calculate_totient(d)


def euler_problem_72():
    print(int(total))


if __name__ == "__main__":
    euler_problem_72()
