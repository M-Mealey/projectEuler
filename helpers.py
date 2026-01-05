import math
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(x):
    if not isinstance(x, int) or x<=1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

"""
Input integer x, returns list of positive integer divisors of x
O(root(x)) time
"""
def find_divisors(x):
    divisors = [1]
    for i in range(2, int(math.sqrt(x)+1)):
        if x%i==0:
            divisors.append(i)
            if x/i != i:
                divisors.append(int(x/i))
    divisors.sort()
    return divisors

"""
Sieve of Eratosthenes - Generate primes up to (exclusive) a given number by iterating over list from low to high,
for each entry in list remove all multiples of it
"""
def prime_sieve(limit):
    is_prime_list = [True] * limit
    is_prime_list[0] = False
    is_prime_list[1] = False
    current_i = 2
    while current_i <= math.ceil(math.sqrt(limit)):
        if is_prime_list[current_i]:
            for j in range(2*current_i, limit, current_i):
                is_prime_list[j] = False
        current_i += 1
    return [x for x,prime in enumerate(is_prime_list) if prime]

# from problem 33
# Find GCD of 2 integers using Euclidean algorithm
def gcd(n1, n2):
    a, b = max(n1, n2), min(n1, n2)
    r = a%b
    while r!=0:
        a, b = b, r
        r = a%b
    return b
