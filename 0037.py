"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from helpers import is_prime

# for given int x, checks if all left and right truncations are prime. Returns True or False.
def check_truncs(x):
    n = 1
    while n<len(str(x)):
        if not is_prime(x % (10**n)):
            return False
        if not is_prime(x // (10**n)):
            return False
        n += 1
    return True

answers = []
for i in range(10, 1000000):
    if is_prime(i) and check_truncs(i):
        answers.append(i)

print(sum(answers))