"""
Project Euler Problem 108
=========================

In the following equation x, y, and n are positive integers.

                                1 + 1 = 1
                                x   y   n

For n = 4 there are exactly three distinct solutions:

                                1 + 1  = 1
                                5   20   4
                                1 + 1  = 1
                                6   12   4
                                1 + 1  = 1
                                8   8    4

What is the least value of n for which the number of distinct solutions
exceeds one-thousand?

NOTE: This problem is an easier version of problem 110; it is strongly
advised that you solve this one first.
"""
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve
import math
import itertools

MAX_N = 200000
PRIMES = prime_sieve(MAX_N)
PRIME_FACTORIZATIONS = {1: {1}, 2: {2}, 3: {3}, 4: {2, 4}}


def get_number_from_pf_array(arr):
    """ calculate an int from the array representing the powers of its prime factorization """
    total = 1
    for i, n in enumerate(arr):
        total *= PRIMES[i]**n
    return total


def get_num_factors_from_pf_array(arr):
    """ calculate the number of factors an int has using its prime factorization array """
    return math.prod(x+1 for x in arr)


def solve():
    """ solve problem 108
    blog here:
    https://blog.melindalu.com/posts/2013-01-09-project-euler-108-diophantine-reciprocals/
    shows that number of solutions is equal to number of unique pairs of factors for n^2
    In other words, we're looking for the smallest n for which n^2 has at least 2000 factors
    Can find the number of factors a number has from its prime factorization:
    https://www.cut-the-knot.org/blue/NumberOfFactors.shtml
    Therefore, can represent each n as a list of exponents [e1, e2, e3, ... ei]
    where n = 2^e1 * 3^e2 * 5^e3 ... pi^ei
    n^2 doubles all exponents
    solve by iterating over these exponent lists, find simple solution [1,1,...1] and
    then optimize?"""
    # try all arrays up to length 6, power up to 6?
    # looking for a square number so all powers must be even
    # could optimize further by stopping iteration when remaining permutations
    # are bigger than current?
    powers = {0, 2, 4, 6}
    perms = list(itertools.product(powers, repeat=6))
    min_n_squared = 1000000000000000000
    for i in perms:
        if get_num_factors_from_pf_array(i) > 2000:
            min_n_squared = min(min_n_squared, get_number_from_pf_array(i))
    return int(math.sqrt(min_n_squared))


if __name__ == "__main__":
    print(solve())
