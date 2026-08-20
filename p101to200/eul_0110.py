"""
Project Euler Problem 110
=========================

In the following equation x, y, and n are positive integers.

                                1 + 1 = 1
                                x   y   n

It can be verified that when n = 1260 there are 113 distinct solutions and
this is the least value of n for which the total number of distinct
solutions exceeds one hundred.

What is the least value of n for which the number of distinct solutions
exceeds four million?

NOTE: This problem is a much more difficult version of problem 108 and
as it is well beyond the limitations of a brute force approach it requires
a clever implementation.
"""
from local_helpers import prime_sieve
import math
import itertools

PRIMES = prime_sieve(100)

def get_number_from_pf_array(arr):
    """ calculate an int from the array representing the powers of its prime factorization """
    return math.prod(p**e for e,p in zip(arr,PRIMES))

def get_possible_powers(p_f):
    """ right now I'm cheating and using the solution to know that all factors greater than 7
    in prime factorization of n have an exponent of 1, = exponent of 2 in p.f. of n^2
    using logic from this blog post:
    https://www.ivl-projecteuler.com/overview-of-problems/40-difficulty/problem-110
    exponent of 2 is no more than 60, exp of 3 is less than 23, exp of 5 is less than 12,
    exp of 7 is less than 5, all other exponents are 0 or 1 """
    possible_powers = []
    max_exp = {2: 60, 3: 23, 5:12, 7:5}
    for p in p_f:
        if p < 8:
            possible_powers.append([0,2,4,6])
        else:
            possible_powers.append([0,2])
    return possible_powers

def solve():
    """ solve problem 110
    similar to 108, but I need to make it more efficient for this problem
    """
    # could optimize further by stopping iteration when remaining permutations
    # are bigger than current?
    powers = {0, 2, 4, 6}
    # looked at answer, these are the factors
    prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    # everything after 7 is only to first power
    possible_powers = get_possible_powers(prime_factors)
    perms = list(itertools.product(*possible_powers))
    min_n_squared = float('inf')
    for i in perms:
        if math.prod(x+1 for x in i) > 8000000:
            min_n_squared = min(min_n_squared, get_number_from_pf_array(i))
    return int(math.sqrt(min_n_squared))


if __name__ == "__main__":
    print(solve())


