"""
Helper functions for Project Euler problems
"""


import math
import random
from functools import lru_cache


@lru_cache(maxsize=None)
def is_prime(x):
    """ check if a number is prime through division """
    if not isinstance(x, int) or x <= 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


def find_divisors(x):
    """
    Input integer x, returns list of positive integer divisors of x
    O(root(x)) time
    """
    divisors = [1]
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            divisors.append(i)
            if x/i != i:
                divisors.append(int(x/i))
    divisors.sort()
    return divisors


def prime_sieve(limit):
    """
    Sieve of Eratosthenes - Generate primes up to (exclusive) a given number
    by iterating over list from low to high,
    for each entry in list remove all multiples of it
    """
    is_prime_list = [True] * limit
    is_prime_list[0] = False
    is_prime_list[1] = False
    current_i = 2
    while current_i <= math.ceil(math.sqrt(limit)):
        if is_prime_list[current_i]:
            for j in range(2*current_i, limit, current_i):
                is_prime_list[j] = False
        current_i += 1
    return [x for x, prime in enumerate(is_prime_list) if prime]


def gcd(n1, n2):
    """ Find GCD of 2 integers using Euclidean algorithm """
    a, b = max(n1, n2), min(n1, n2)
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


def miller_rabin_prime_test(n, k=40):
    """ Miller Rabin primality test
    code copied from: https://gist.github.com/Ayrx/5884790
    with some modifications"""

    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # pylint: disable-next=line-too-long
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def create_totient_dict(upper_limit):
    """ creates a dictionary with integer keys up to upper limit with totient fuction as value
     Used by problems 69 and 72 """

    def find_next_factor(x):
        """ find the smallest factor of int n,
        then return the highest power of it that divides n """
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                factor = i
                while (x // factor) % i == 0:
                    factor *= i
                return factor
        return x

    def calculate_totient(n, calculated_totients):
        """ calculate the totient for int n"""
        f1 = find_next_factor(n)
        f2 = n // f1
        return int(calculated_totients[f1] * calculated_totients[f2])

    calculated_totients = {2: 1, 3: 2, 4: 2, 5: 4, 6: 2, 7: 6, 8: 4}
    primes = set(prime_sieve(1000000))
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
        tot = calculate_totient(d, calculated_totients)
        calculated_totients[d] = tot
    return calculated_totients
