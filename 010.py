"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

# copied from problem 3 solution, checks if x is prime
def is_prime(x):
    if x<=1:
        return False
    result = True
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            result = False
            break
    return result

sum = 17
for i in range(2000000):
    if is_prime(i):
        sum += i
print(sum)
