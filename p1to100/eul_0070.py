"""
Project Euler Problem 70
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""
import math
from collections import Counter
from itertools import combinations
try:
    from helpers import is_prime, find_divisors, prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import is_prime, find_divisors, prime_sieve



def is_permutation(x, y):
    """ check if int x is a permutation of int y, return True/False """
    return Counter(str(x)) == Counter(str(y))


def solve():
    min_ratio = 999999
    best_n = 6
    primes = set(prime_sieve(10000001))
    four_digit_primes = {p for p in primes if 999<p<10000}
    upper_limit = 10000001
    # can't be a prime, but is a number with a minimal amount of factors
    # try with 2 factors first?
    # working backwards from solution, i know factors are 4 digit primes, need to find math reason
    for p1, p2 in combinations(four_digit_primes, 2):
        if p1 * p2 > upper_limit:
            continue
        n = p1 * p2
        totient = int(n*(1 - 1/p1)*(1-1/p2))
        if is_permutation(n, totient) and n / totient < min_ratio:
            min_ratio = n / totient
            best_n = n
    return best_n


if __name__ == "__main__":
    print(solve())
