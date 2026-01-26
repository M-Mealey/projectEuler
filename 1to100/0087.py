"""
Project Euler Problem 87
========================

The smallest number expressible as the sum of a prime square, prime cube,
and prime fourth power is 28. In fact, there are exactly four numbers
below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a
prime square, prime cube, and prime fourth power?
"""
import math
from local_helpers import prime_sieve

max_sum = 50000000
prime_squares = prime_sieve(math.ceil(max_sum**0.5))
prime_cubes = prime_sieve(math.ceil(max_sum**(1/3)))
prime_quads = prime_sieve(math.ceil(max_sum**0.25))

numbers = set()

for x in prime_squares:
    for y in prime_cubes:
        for z in prime_quads:
            sums = x**2 + y**3 + z**4
            if sums < 50000000:
                numbers.add(sums)

print(len(numbers))

