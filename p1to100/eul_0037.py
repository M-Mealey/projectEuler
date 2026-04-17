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
try:
    from helpers import is_prime, prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import is_prime, prime_sieve


def check_truncs(x, p_set):
    """
    for given int x, checks if all left and right truncations are prime. Returns True or False.
    :param x: an integer
    :param p_set: a set of all the primes to check
    :return: True if all left and right truncations are prime, otherwise False
    """
    if len(str(x)) == 1:
        return False
    n = 1
    while n < len(str(x)):
        if x % (10**n) not in p_set:
            return False
        if x // (10**n) not in p_set:
            return False
        n += 1
    return True


def solve():
    """ solve problem 37 """
    prime_set = set(prime_sieve(1000000))
    answers = []
    for i in prime_set:
        if check_truncs(i, prime_set):
            answers.append(i)
    return sum(answers)


if __name__ == "__main__":
    print(solve())
