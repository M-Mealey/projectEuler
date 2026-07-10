"""
Project Euler Problem 69
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of numbers less than n which are relatively
prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, f(9)=6.

+------------------------------------------+
| n  | Relatively Prime | f(n) | n/f(n)    |
|----+------------------+------+-----------|
| 2  | 1                | 1    | 2         |
|----+------------------+------+-----------|
| 3  | 1,2              | 2    | 1.5       |
|----+------------------+------+-----------|
| 4  | 1,3              | 2    | 2         |
|----+------------------+------+-----------|
| 5  | 1,2,3,4          | 4    | 1.25      |
|----+------------------+------+-----------|
| 6  | 1,5              | 2    | 3         |
|----+------------------+------+-----------|
| 7  | 1,2,3,4,5,6      | 6    | 1.1666... |
|----+------------------+------+-----------|
| 8  | 1,3,5,7          | 4    | 2         |
|----+------------------+------+-----------|
| 9  | 1,2,4,5,7,8      | 6    | 1.5       |
|----+------------------+------+-----------|
| 10 | 1,3,7,9          | 4    | 2.5       |
+------------------------------------------+

It can be seen that n=6 produces a maximum n/f(n) for n 10.

Find the value of n 1,000,000 for which n/f(n) is a maximum.
"""

try:
    from helpers import prime_sieve, create_totient_dict  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve, create_totient_dict

primes = set(prime_sieve(1000000))


def solve(upper_limit=1000001):
    """ solve problem 69 """
    tot_dict = create_totient_dict(upper_limit)

    max_ratio = 0
    best_n = 2
    for n, f_n in tot_dict.items():
        ratio = n/f_n
        if ratio > max_ratio:
            max_ratio = ratio
            best_n = n
    return best_n


if __name__ == "__main__":
    print(solve())
