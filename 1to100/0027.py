"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
from local_helpers import is_prime

# for a given generator g, find how many sequential primes it yields starting from the first element
# returns int, the number of sequential primes
def find_sequential_primes(g):
    count = 0
    while is_prime(next(g, None)):
        count += 1
    return count

# vars to keep track of best answer so far
max_n = 10 # maximum value of n to try, can be increased
max_sequence = 0
best_pair = None

# iterate over 0<=a<1000 and 0<=b<1000, check combinations of +-a, +-b for each
for a in range(1000):
    for b in range(1000):
        if not is_prime(abs(b)):
            continue # if b is composite, the first number produced (n=0) will be composite
        tuples = [(a,b), (a, -b), (-a, b), (-a, -b)]
        for a0,b0 in tuples:
            sequence = find_sequential_primes((n*n + a0*n + b0 for n in range(max_n)))
            if sequence == max_n: # all entries were prime, need to increase max_n
                max_n += 10
                tuples.append((a0,b0)) # add tuple back to list, retry later
            if sequence > max_sequence:
                best_pair = (a0,b0)
                max_sequence = sequence

#print(f"best pair: a={best_pair[0]}, b={best_pair[1]}")
#print(f"max sequence: {max_sequence}")
print(best_pair[0] * best_pair[1])