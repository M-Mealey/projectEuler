"""
Project Euler Problem 118
=========================

Using all of the digits 1 through 9 and concatenating them freely to form
decimal integers, different sets can be formed. Interestingly with the set
{2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine
exactly once contain only prime elements?
"""
import itertools
from functools import reduce

from local_helpers import prime_sieve, miller_rabin_prime_test

# primes up to 6 digits are not to expensive to compute, start with max of 6 digits
PRIMES = set(prime_sieve(1000000))

def solve():
    """ solve problem 118 """
    # no 9-digit prime because digits add to 45, 45%3 = 0
    candidate_primes = set()
    candidate_prime_dict = {}
    for p in PRIMES:
        digits = [int(d) for d in str(p)]
        digits.sort()
        digit_set = set(digits)
        if 0 not in digit_set and len(digits) == len(digit_set):
            candidate_primes.add(p)
            digit_tup = tuple(digits)
            if digit_tup in candidate_prime_dict:
                candidate_prime_dict[digit_tup].append(p)
            else:
                candidate_prime_dict[digit_tup] = [p]
    print(candidate_prime_dict)

    # sets with an 8 digit prime: the other prime is 1 digit
    # can't be 3 b/c digits of 8-digit num would add to 42
    set_count = 0
    ds = {1,2,3,4,5,6,7,8,9}
    for i in (2,5,7):
        remaining_digits = ds - {i}
        possible = itertools.permutations(remaining_digits)
        for p in possible:
            p_int = reduce(lambda total, digit: total * 10 + digit, p)
            if miller_rabin_prime_test(p_int):
                set_count += 1
    print(set_count)

    for single_pair in itertools.combinations([2,3,5,7], 2):
        if single_pair in candidate_prime_dict:
            candidate_prime_dict[single_pair].append(list(single_pair))
        else:
            candidate_prime_dict[single_pair] = list(single_pair)

    two_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 2}

    # 7 digit prime: must be paired with 2 other digits
    print(two_digit_primes)

    for k,v in two_digit_primes.items():
        remaining_digits = {1,2,3,4,5,6,7,8,9} - set(k)
        possible = itertools.permutations(remaining_digits)
        for p in possible:
            p_int = reduce(lambda total, digit: total * 10 + digit, p)
            if miller_rabin_prime_test(p_int):
                set_count += len(v)

    print(set_count)
    # dict is ordered, iterate in order removing explored keys to prevent duplicates
    #for k, v in candidate_prime_dict.items():
    #    print(k)
    #    print(v)

    return -1

if __name__ == "__main__":
    print(solve())
