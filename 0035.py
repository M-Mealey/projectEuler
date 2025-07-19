"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math

# copied from problem 10 solution and modified, checks if x is prime
def is_prime(x):
    if not isinstance(x, int) or x<=1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

# for input int x, returns list of ints containing "rotations" of x
def get_rotations(x):
    rotations = []
    num_rotations = len(str(x))
    x_string = str(x)
    for i in range(1, num_rotations):
        next_str_r = x_string[i:] + x_string[:i]
        rotations.append(int(next_str_r))
    return rotations

circular_primes = 13 # there are 13 below 100, this var tracks total number found
# check every odd number between 100 and 1 million
for i in range(101, 1000000, 2):
    # if there is an even digit, then the rotation with that digit in the ones place won't be prime
    evens = [e for e in str(i) if e in "02468"]
    if len(evens) == 0 and is_prime(i):
        rot = get_rotations(i)
        prime_rotations = [is_prime(x) for x in get_rotations(i)]
        if False not in prime_rotations:
            circular_primes += 1

print(circular_primes)
