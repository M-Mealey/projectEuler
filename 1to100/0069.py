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
import math
from local_helpers import is_prime

# Copied from problem 47


def find_next_factor(x):
    if not isinstance(x, int) or x <= 1:
        return -1
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return i
    return x

# Copied from problem 47 and modified


def find_prime_factors(x):
    factors = set()
    f = find_next_factor(x)
    while f > 0:
        factors.add(f)
        x = int(x/f)
        f = find_next_factor(x)
    return factors


def calculate_totient(n):
    prime_factors = find_prime_factors(n)
    totient = n
    for p in prime_factors:
        totient *= (1 - 1/p)
    return totient


max_ratio = 3
best_n = 6
for n in range(7, 1000001):
    if is_prime(n):
        # a prime will never be the answer. for prime n, n/f(n) = n/(n-1) < 2
        continue
    ratio = n / calculate_totient(n)
    if ratio > max_ratio:
        max_ratio = ratio
        best_n = n


def euler_problem_69():
    print(best_n)


if __name__ == "__main__":
    euler_problem_69()
