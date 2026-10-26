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
    #print(candidate_prime_dict)

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
    print(f"set count after 8+1: {set_count}")



    #print(set_count)
    # dict is ordered, iterate in order removing explored keys to prevent duplicates
    #for k, v in candidate_prime_dict.items():
    #    print(k)
    #    print(v)
    def combine_dicts_mult(d1, d2):
        combined_d = {}
        for k1, v1 in d1.items():
            for k2, v2 in d2.items():
                intersection = tuple(set(k1) & set(k2))
                if len(intersection) > 0:
                    continue
                d_set = set(k1) | set(k2)
                d_tup = tuple(sorted(d_set))
                values = set()
                for l1 in v1:
                    for l2 in v2:
                        values.add(tuple(sorted(l1+l2)))
                if d_tup not in combined_d:
                    combined_d[d_tup] = values
                else:
                    old_values = combined_d[d_tup]
                    new_values = old_values | values
                    combined_d[d_tup] = new_values
        return combined_d



    def combine_dicts_add(d1, d2):
        combined_d = dict(d1) # this makes a deep copy, maybe shallow copy would work?
        for k, v in d2.items():
            if k in combined_d:
                combined_d[k] = combined_d[k] | v
            else:
                combined_d[k] = v

        return combined_d

    one_digit_primes = {(2,): {(2,)}, (3,): {(3,)}, (5,): {(5,)}, (7,): {(7,)}}
    print("HERE")
    print(combine_dicts_mult(one_digit_primes, one_digit_primes))

    two_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 2}

    two_digit_combos = combine_dicts_add(two_digit_primes, combine_dicts_mult(one_digit_primes, one_digit_primes))

    print(two_digit_primes)
    print(two_digit_combos)


    # 7 digit prime: must be paired with 2 other digits
    for k, v in two_digit_combos.items():
        remaining_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(k)
        possible = itertools.permutations(remaining_digits)
        for p in possible:
            p_int = reduce(lambda total, digit: total * 10 + digit, p)
            if miller_rabin_prime_test(p_int):
                set_count += len(v)
    print(f"set count after 7: {set_count}")

    three_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 3}
    three_digit_combos = combine_dicts_add(three_digit_primes,
                                           combine_dicts_mult(one_digit_primes, two_digit_combos))

    print(three_digit_combos)

    # to get four you can do 1+3 or 2+2
    one_by_three = combine_dicts_mult(one_digit_primes, three_digit_combos)
    two_by_two = combine_dicts_mult(two_digit_combos, two_digit_combos)
    composite_fours = combine_dicts_add(one_by_three, two_by_two)

    four_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 4}
    four_digit_combos = combine_dicts_add(four_digit_primes, composite_fours)

    #print(four_digit_combos)


    # five is 1+4 or 2+3
    one_by_four = combine_dicts_mult(one_digit_primes, four_digit_combos)
    two_by_three = combine_dicts_mult(two_digit_combos, three_digit_combos)
    composite_fives = combine_dicts_add(one_by_four, two_by_three)

    five_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 5}
    five_digit_combos = combine_dicts_add(five_digit_primes, composite_fives)

    #print(five_digit_combos)

    # six is 1+5, 2+4, or 3+3
    one_by_five = combine_dicts_mult(one_digit_primes, five_digit_combos)
    two_by_four = combine_dicts_mult(two_digit_combos, four_digit_combos)
    three_by_three = combine_dicts_mult(three_digit_combos, three_digit_combos)
    composite_sixes = combine_dicts_add(one_by_five, combine_dicts_add(two_by_four, three_by_three))

    six_digit_primes = {k: v for k, v in candidate_prime_dict.items() if len(k) == 6}
    six_digit_combos = combine_dicts_add(six_digit_primes, composite_sixes)

    set_count_6a=0
    for k, v in three_digit_combos.items():
        #print(k)
        remaining_digits = {1, 2, 3, 4, 5, 6, 7, 8, 9} - set(k)
        possible = itertools.permutations(remaining_digits)
        for p in possible:
            p_int = reduce(lambda total, digit: total * 10 + digit, p)
            if p_int in candidate_primes:
                #print(f"\t{p_int}")
                #set_count += len(v)
                set_count_6a += len(v)
    print(f"set count after 6: {set_count}")



    # now add to get 9. 8+1 and 7+2 are already done
    #print(set_count)
    sbt1 = combine_dicts_mult(six_digit_primes, three_digit_combos)
    print(sbt1)
    six_by_three = combine_dicts_mult(six_digit_combos, three_digit_combos)
    print("six digit cobmos")
    print(six_digit_combos)
    print("six by three")
    print(six_by_three)


    five_by_four = combine_dicts_mult(five_digit_combos, four_digit_combos)

    big_one = combine_dicts_add(six_by_three, five_by_four)
    big_count = 0
    for i in big_one.values():
        set_count+=len(i)
    print(f"big count: {big_count}")



    return set_count

if __name__ == "__main__":
    print(solve())
