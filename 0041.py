"""
Project Euler Problem 41
========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools
import math

def is_prime(x):
    if not isinstance(x, int) or x<=1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

# can only go up to 9-digit
largest = 2143
for n in range(4,10):
    perms = itertools.permutations(range(1,n+1))
    for p in perms:
        x = sum(list(k * (10**(n-p.index(k)-1)) for k in p))
        if is_prime(x):
            largest = max(largest, x)

print(largest)
