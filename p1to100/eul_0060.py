"""
Project Euler Problem 60
========================

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
primes and concatenating them in any order the result will always be
prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The
sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
"""
from itertools import combinations
try:
    from helpers import miller_rabin_prime_test, prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import miller_rabin_prime_test, prime_sieve

MAX_PRIME = 2000000
prime_list = prime_sieve(MAX_PRIME)
primes = set(prime_list)
primes.remove(5)  # only prime that ends in 5 is 5


def check_prime_pair(x, y):
    """ check whether two primes concatenate to form another prime """
    p1, p2 = int(f"{x}{y}"), int(f"{y}{x}")
    if p1 in primes and p2 in primes:
        return True
    return miller_rabin_prime_test(p1) and miller_rabin_prime_test(p2)


def verify_set(p_l, p_lookup):
    """ verify that numbers in p_list satisfy the problem """
    for p1, p2 in combinations(p_l, 2):
        if p1 not in p_lookup[p2] or p2 not in p_lookup[p1]:
            return False
    return True


def solve():
    """ solve problem 60 """

    visited_primes = set()
    prime_pair_lookup = {}
    pairs_found = {}
    for p in prime_list:
        prime_pair_lookup[p] = set()
        pairs_found[p] = 0
        for v in visited_primes:
            if check_prime_pair(p, v):
                prime_pair_lookup[v].add(p)
                prime_pair_lookup[p].add(v)
                pairs_found[p] += 1
                pairs_found[v] += 1
        visited_primes.add(p)
        if pairs_found[p] >= 4:
            pair_list = [x for x in prime_pair_lookup[p] if pairs_found[x] >= 4 and len(
                prime_pair_lookup[x].intersection(prime_pair_lookup[p])) >= 3]
            if len(pair_list) >= 4:
                for p_combo in combinations(pair_list, 4):
                    p_list = list(p_combo)
                    p_list.append(p)
                    if verify_set(p_list, prime_pair_lookup):
                        return sum(p_list)
    return -1


if __name__ == "__main__":
    print(solve())
