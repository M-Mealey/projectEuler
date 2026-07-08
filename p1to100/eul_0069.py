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
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve

primes = set(prime_sieve(1000000))
calculated_totients = {2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6, 8: 4}


def find_next_factor(x):
    """ find the smallest factor of int n, then return the highest power of it that divides n """
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            factor = i
            while (x//factor) % i == 0:
                factor *= i
            return factor
    return x


def calculate_totient(n):
    """ calculate the totient for int n"""
    f1 = find_next_factor(n)
    f2 = n//f1
    return int(calculated_totients[f1] * calculated_totients[f2])


def solve(upper_limit=1000001):
    """ solve problem 69 """

    for d in range(2, upper_limit):
        if d in primes:
            tot = d - 1
            calculated_totients[d] = tot
            next_power = d * d
            while next_power < upper_limit:
                tot *= d
                calculated_totients[next_power] = tot
                next_power *= d
        if d in calculated_totients:
            continue
        tot = calculate_totient(d)
        calculated_totients[d] = tot
    max_ratio = 0
    best_n = 2
    for n in calculated_totients:
        ratio = n/calculated_totients[n]
        if ratio > max_ratio:
            max_ratio = ratio
            best_n = n
    return best_n


if __name__ == "__main__":
    print(solve())
