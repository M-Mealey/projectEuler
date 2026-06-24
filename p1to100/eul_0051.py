"""
Project Euler Problem 51
========================

By replacing the 1st digit of *57, it turns out that six of the possible
values: 157, 257, 457, 557, 757, and 857, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this
5-digit number is the first example having seven primes, yielding the
family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently
56003, being the first member of this family, is the smallest prime with
this property.

Find the smallest prime which, by replacing part of the number (not
necessarily adjacent digits) with the same digit, is part of an eight
prime value family.
"""

try:
    from helpers import is_prime  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import is_prime
import itertools


def int_to_tup(n):
    """
    convert int to its tuple representation
    """
    return tuple((n % (10 ** b)) // (10 ** (b - 1)) for b in range(len(str(n)), 0, -1))


def test_map(num, tmap):
    """ test if all numbers in map are prime? """
    # skip maps of all 0 or all 1
    if 1 not in tmap or 0 not in tmap:
        return False
    num_tup = int_to_tup(num)
    strikes = 0
    smallest_prime = 999999999999
    for x in range(10):
        if x == 0 and tmap[0] == 1:
            strikes += 1
            continue
        total = 0
        for i, m in enumerate(tmap):
            total *= 10
            if m == 0:
                total += num_tup[i]
            else:
                total += x
        if not is_prime(total):
            strikes += 1
        else:
            smallest_prime = min(smallest_prime, total)
        if strikes >= 3:
            return False
    return smallest_prime


def solve():
    """ solve problem 51 """
    solution = 0
    prime_list = [x for x in range(100000, 200000) if is_prime(x)]
    for i in prime_list:
        num_digits = len(str(i))
        # generate all possible positions for *s, 1 = *, 0 = keep digit
        digit_maps = itertools.product((0, 1), repeat=num_digits)
        for m in digit_maps:
            if test_map(i, m):
                solution = test_map(i, m)
                break
        if solution:
            break
    return solution


if __name__ == "__main__":
    print(solve())
