"""
Project Euler Problem 72
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper
fractions for d 1,000,000?
"""

# how many fractions don't reduce?
# won't reduce when numerator is relatively prime, so for denominator d
# the number of elements it adds to the set is the number of integers >d that are relatively prime
# aka totient
import math
try:
    from helpers import prime_sieve  # pylint: disable=E0611
except ModuleNotFoundError:
    from local_helpers import prime_sieve

primes = set(prime_sieve(1000000))
calculated_totients = {1:1, 2:1, 3:2, 4:2, 5:4, 6:2, 7:6, 8:4}

def find_next_factor(x):
    """ find the smallest factor of int n """
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return i
    return x


def calculate_totient(n):
    """ calculate the totient for int n """
    f1 = find_next_factor(n)
    f2 = n//f1
    return calculated_totients[f1] * calculated_totients[f2]




def solve():
    """ solve problem 72 """
    total = 21
    numbers_to_visit = set(range(9,1000001))
    # visit prime numbers and their powers first, totient is easy to calculate
    for p in primes:
        tot = p-1
        calculated_totients[p] = tot
        if p>9:
            numbers_to_visit.remove(p)
            total += tot
        tot = p-1
        next_power = p*p
        while next_power < 1000001:
            tot *= p
            calculated_totients[next_power] = tot
            if next_power > 9:
                numbers_to_visit.remove(next_power)
                total += tot
            next_power *= p
    numbers_to_visit = sorted(numbers_to_visit, reverse=True)
    while len(numbers_to_visit) > 0:
        d = numbers_to_visit.pop()
        tot = calculate_totient(d)
        calculated_totients[d] = tot
        total += tot
    return int(total)


if __name__ == "__main__":
    print(solve())
