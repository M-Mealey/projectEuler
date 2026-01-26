"""
Project Euler Problem 70
========================

Euler's Totient function, f(n) [sometimes called the phi function], is
used to determine the number of positive numbers less than or equal to n
which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
all less than nine and relatively prime to nine, f(9)=6.
The number 1 is considered to be relatively prime to every positive
number, so f(1)=1.

Interestingly, f(87109)=79180, and it can be seen that 87109 is a
permutation of 79180.

Find the value of n, 1 < n < 10^7, for which f(n) is a permutation of n
and the ratio n/f(n) produces a minimum.
"""
import math
from local_helpers import is_prime

# Copied from problem 47
def find_next_factor(x):
    if not isinstance(x, int) or x<=1:
        return -1
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return i
    return x

# Copied from problem 47 and modified
def find_prime_factors(x):
    factors = set()
    f = find_next_factor(x)
    while f>0:
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


# the stuff above was copied from last project, this is the only new function
# checks if int x is a permutation of int y
def is_permutation(x, y):
    x_digits = [d for d in str(x)]
    y_digits = [d for d in str(y)]
    x_digits.sort()
    y_digits.sort()
    if x_digits == y_digits:
        return True
    return False

min_ratio = 999999
best_n = 6
for n in range(7, 10000001):
    if is_prime(n):
        continue # a prime will never be the answer. for prime n, f(n) = (n-1), can't be a permutation of n
    totient = int(calculate_totient(n))
    if is_permutation(n, totient) and n/totient < min_ratio:
        min_ratio = n/totient
        best_n = n
print(best_n)

