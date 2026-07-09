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

from eul_0069 import create_totient_dict
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve

primes = set(prime_sieve(1000000))


def solve(upper_limit=1000001):
    """ solve problem 72 """
    calculated_totients = create_totient_dict(upper_limit)

    return sum(calculated_totients.values())


if __name__ == "__main__":
    print(solve())
