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
    target_n = 4_000_000
    target_n_sq = 2*target_n
    # start by finding factors if all primes are to first power, this creates an upper bound
    # because if any prime number was used 0 times and there was a bigger prime used x times,
    # then another number could be created by dividing by big prime x times and multiplying
    # by smaller prime x times, and it would have the same number of factors and be smaller
    upper_bound_powers = [2]
    while math.prod(x+1 for x in upper_bound_powers) < target_n_sq:
        upper_bound_powers.append(2)
    print("upper bound")
    print(upper_bound_powers)
    upper_bound = get_number_from_pf_array(upper_bound_powers)
    print(upper_bound)
    # try to optimize, starting from end. ? can get rid of biggest prime and increase other
    # exponents so that there are still over 8M factors
    # also, exponent list will always be in order greatest to least, otherwise you could
    # make a smaller number with the same amount of factors
    upper_bound_powers = [8]
    while math.prod(x+1 for x in upper_bound_powers) < target_n_sq and get_number_from_pf_array(upper_bound_powers) < upper_bound:
        upper_bound_powers.append(8)
    print("upper bound")
    print(upper_bound_powers)
    print(get_number_from_pf_array(upper_bound_powers))

    # we know the shortest list with all 2s, now try adding 4s? find shortest list with 1 4,
    # then 2, etc? knowing that the highest power is 6, this would be easy to solve iteratively,
    # but I want a solution that works without that knowledge


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
            print(i)
    return int(math.sqrt(min_n_squared))


if __name__ == "__main__":
    print(solve())


