"""
Project Euler Problem 111
=========================

Considering 4-digit primes containing repeated digits it is clear that
they cannot all be the same: 1111 is divisible by 11, 2222 is divisible by
22, and so on. But there are nine 4-digit primes containing three ones:

           1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated digits
for an n-digit prime where d is the repeated digit, N(n, d) represents the
number of such primes, and S(n, d) represents the sum of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit
prime where one is the repeated digit, there are N(4, 1) = 9 such primes,
and the sum of these primes is S(4, 1) = 22275. It turns out that for d =
0, it is only possible to have M(4, 0) = 2 repeated digits, but there are
N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

                +----------------------------------------+
                | Digit, d | M(4, d) | N(4, d) | S(4, d) |
                |----------+---------+---------+---------|
                | 0        | 2       | 13      | 67061   |
                |----------+---------+---------+---------|
                | 1        | 3       | 9       | 22275   |
                |----------+---------+---------+---------|
                | 2        | 3       | 1       | 2221    |
                |----------+---------+---------+---------|
                | 3        | 3       | 12      | 46214   |
                |----------+---------+---------+---------|
                | 4        | 3       | 2       | 8888    |
                |----------+---------+---------+---------|
                | 5        | 3       | 1       | 5557    |
                |----------+---------+---------+---------|
                | 6        | 3       | 1       | 6661    |
                |----------+---------+---------+---------|
                | 7        | 3       | 9       | 57863   |
                |----------+---------+---------+---------|
                | 8        | 3       | 1       | 8887    |
                |----------+---------+---------+---------|
                | 9        | 3       | 7       | 48073   |
                +----------------------------------------+

For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""

def get_int(d_list, d, wc):
    total = 0
    wc_iter = iter(wc)
    for p in d_list:
        total *= 10
        if p=='d':
            total += d
        elif p=='*':
            total += next(wc_iter)
    return total

from local_helpers import miller_rabin_prime_test, prime_sieve
import itertools
from sympy import isprime

# check if M(10, d) == 9
# won't be the case for d=0
# create permutations of d, *

m_dict = {}
s_dict = {}
digits_completed = set()
m_candidate = 9
while m_candidate > 1 and len(digits_completed) < 10:
    number_templates = ['d'] * m_candidate + ['*'] * (10-m_candidate)
    unique_perms = set(itertools.permutations(number_templates))
    for d in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if d in digits_completed:
            continue
        print(f"d={d}")
        wildcard_digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
        wildcard_digits.remove(d)
        wildcard_combos = itertools.product(wildcard_digits, repeat=10-m_candidate)
        results = [[get_int(p, d, w) for w in wildcard_combos] for p in unique_perms]
        prime_results = [x for l in results for x in l if x > 999999999 and isprime(x)]
        if len(prime_results) > 0:
            digits_completed.add(d)
            m_dict[d] = m_candidate
            s_dict[d] = sum(prime_results)
    m_candidate -= 1
print(m_dict)
print(s_dict)


