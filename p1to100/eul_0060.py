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

MAX_PRIME = 20000
primes = prime_sieve(MAX_PRIME)
primes.remove(5)  # only prime that ends in 5 is 5


def check_prime_pair(x, y):
    """ check whether two primes concatenate to form another prime """
    return miller_rabin_prime_test(int(str(x)+str(y))) and miller_rabin_prime_test(int(str(y)+str(x)))


def solve():
    """ solve problem 60 """
    all_prime_pairs = list(combinations(primes, 2))
    print(all_prime_pairs)
    prime_pair_lookup = {x:[] for x in primes}
    print(prime_pair_lookup)
    for p1, p2 in all_prime_pairs:
        if check_prime_pair(p1, p2):
            prime_pair_lookup[p1].append(p2)
    for k in prime_pair_lookup:
        if len(prime_pair_lookup[k]) >= 4:
            print(k)
            print(prime_pair_lookup[k])

    return -1

    p_sum = 200000
    while len(primes) > 0:
        p = primes.pop(0)
        if p * 5 > p_sum:
            continue
        pairs = [x for x in primes if check_prime_pair(p, x)]
        while len(pairs) > 0:
            pj = pairs.pop(0)
            if p + pj * 4 > p_sum:
                continue
            triples = [x for x in pairs if check_prime_pair(pj, x)]
            while len(triples) > 0:
                pt = triples.pop(0)
                if p + pj + pt * 3 > p_sum:
                    continue
                quads = [x for x in triples if check_prime_pair(pt, x)]
                while len(quads) > 0:
                    pq = quads.pop(0)
                    if p + pj + pt + pq * 2 > p_sum:
                        continue
                    quints = [x for x in quads if check_prime_pair(pq, x)]
                    if len(quints) > 0:
                        p_sum = min(p_sum, p + pj + pt + pq + quints[0])

    return p_sum


if __name__ == "__main__":
    print(solve())
