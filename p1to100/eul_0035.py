"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve


def get_rotations(x):
    """ for input int x, returns list of ints containing "rotations" of x """
    rotations = []
    num_rotations = len(str(x))
    x_string = str(x)
    for i in range(1, num_rotations):
        next_str_r = x_string[i:] + x_string[:i]
        rotations.append(int(next_str_r))
    return rotations


def solve():
    """ solve problem 35 """
    prime_set = set(prime_sieve(1000000))
    circular_primes = 13  # there are 13 below 100, this var tracks total number found
    # check every odd number between 100 and 1 million
    for i in range(101, 1000000, 2):
        # prime can't have even digit in ones place
        evens = [e for e in str(i) if e in "02468"]
        if len(evens) == 0 and i in prime_set:
            prime_rotations = [x in prime_set for x in get_rotations(i)]
            if False not in prime_rotations:
                circular_primes += 1
    return circular_primes


if __name__ == "__main__":
    print(solve())
