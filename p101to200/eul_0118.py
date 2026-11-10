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

from local_helpers import prime_sieve, miller_rabin_prime_test # pylint: disable=E0611

# primes up to 6 digits are not to expensive to compute, start with max of 6 digits
PRIMES = set(prime_sieve(1000000))

def solve(): # pylint: disable=R0914, R0912, R0915
    """ solve problem 118 """
    set_count = 0

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
                candidate_prime_dict[digit_tup].add((p,))
            else:
                candidate_prime_dict[digit_tup] = {(p,)}


    def combine_dicts_mult(d1, d2):
        combined_d = {}
        d1_keys, d2_keys = set(d1.keys()), set(d2.keys())
        product_set = itertools.product(d1_keys, d2_keys)
        for prod in product_set:
            intersection = tuple(set(prod[0]) & set(prod[1]))
            if len(intersection) > 0:
                continue
            d_set = set(prod[0]) | set(prod[1])
            d_tup = tuple(sorted(d_set))
            values = set()
            for v in itertools.product(d1[prod[0]], d2[prod[1]]):
                values.add(tuple(sorted(v[0] + v[1])))
            combined_d[d_tup] = combined_d.get(d_tup, set()) | values
        return combined_d


    def combine_dicts_add(d1, d2):
        combined_d = d1
        for k, v in d2.items():
            combined_d[k] = combined_d.get(k, set()) | v
        return combined_d

    one_digit_primes = {(2,): {(2,)}, (3,): {(3,)}, (5,): {(5,)}, (7,): {(7,)}}

    two_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 2}
    two_digit_combos = combine_dicts_add(two_digit_primes,
                                         combine_dicts_mult(one_digit_primes, one_digit_primes))

    combo_dicts = [one_digit_primes, two_digit_combos]
    for x in range(3,7):
        x_digit_combos = {}
        x_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == x}
        x_digit_combos = x_digit_primes #if it works fix this
        for i in range(1, (x//2)+1):
            combos = combine_dicts_mult(combo_dicts[i-1], combo_dicts[x-i-1])
            x_digit_combos = combine_dicts_add(x_digit_combos, combos)
        combo_dicts.append(x_digit_combos)


    # sets with an 8 digit prime: the other prime is 1 digit
    # can't be 3 b/c digits of 8-digit num would add to 42
    for i in (2,5,7):
        remaining_digits = {1,2,3,4,5,6,7,8,9} - {i}
        possible = itertools.permutations(remaining_digits)
        for p in possible:
            p_int = reduce(lambda total, digit: total * 10 + digit, p)
            if miller_rabin_prime_test(p_int):
                set_count += 1

    # 7 digit prime: must be paired with 2 other digits
    for k, v in two_digit_combos.items():
        remaining_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(k)
        possible = itertools.permutations(remaining_digits)
        for p in possible:
            p_int = reduce(lambda total, digit: total * 10 + digit, p)
            if miller_rabin_prime_test(p_int):
                set_count += len(v)

    # now add 6+3 and 4+5 to get combos for 9
    six_by_three = combine_dicts_mult(combo_dicts[5], combo_dicts[2])
    five_by_four = combine_dicts_mult(combo_dicts[4], combo_dicts[3])

    for i in combine_dicts_add(six_by_three, five_by_four).values():
        set_count+=len(i)

    return set_count

if __name__ == "__main__":
    print(solve())
