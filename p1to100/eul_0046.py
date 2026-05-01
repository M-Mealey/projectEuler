"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve


def solve():
    twice_squares = [2 * x * x for x in range(1, 1000)]
    prime_set = set(prime_sieve(10000))
    for i in range(3, 10001, 2):
        if not i in prime_set:
            sum_found = False
            for s in twice_squares:
                if s > i:
                    break
                if i - s in prime_set:
                    sum_found = True
            if not sum_found:
                return i


if __name__ == "__main__":
    print(solve())
