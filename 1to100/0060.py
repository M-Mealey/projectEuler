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

from local_helpers import is_prime

max_prime = 20000
primes = [x for x in range(3, max_prime, 2) if is_prime(x)]
primes.remove(5)  # only prime that ends in 5 is 5


def check_prime_pair(x, y):
    return is_prime(int(str(x)+str(y))) and is_prime(int(str(y)+str(x)))


p_sum = 200000
while len(primes) > 0:
    p = primes.pop(0)
    if p*5 > p_sum:
        continue
    pairs = [x for x in primes if check_prime_pair(p, x)]
    while len(pairs) > 0:
        pj = pairs.pop(0)
        if p + pj * 4 > p_sum:
            continue
        triples = [x for x in pairs if check_prime_pair(pj, x)]
        while len(triples) > 0:
            pt = triples.pop(0)
            if p + pj + pt*3 > p_sum:
                continue
            quads = [x for x in triples if check_prime_pair(pt, x)]
            while len(quads) > 0:
                pq = quads.pop(0)
                if p + pj + pt + pq*2 > p_sum:
                    continue
                quints = [x for x in quads if check_prime_pair(pq, x)]
                if len(quints) > 0:
                    p_sum = min(p_sum, p + pj + pt + pq + quints[0])


def euler_problem_60():
    print(p_sum)


if __name__ == "__main__":
    euler_problem_60()
