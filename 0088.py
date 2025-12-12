"""
Project Euler Problem 88
========================

A natural number, N, that can be written as the sum and product of a given
set of at least two natural numbers, {a[1], a[2], ... , a[k]} is called a
product-sum number: N = a[1] + a[2] + ... + a[k] = a[1] * a[2] * ... *
a[k].

For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.

For a given set of size, k, we shall call the smallest N with this
property a minimal product-sum number. The minimal product-sum numbers for
sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2k6, the sum of all the minimal product-sum numbers is 4+6+8+12
= 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2k12 is
{4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2k12000?
"""
from helpers import find_divisors, prime_sieve

# for integer n, finds the unique lengths of all ps sets that can be made for that number
# writes the values to ps_sizes
def find_ps_set_sizes(n, ps_sizes, ps_set=[], the_sum=0, the_prod=1):
    if the_sum > n or the_prod > n:
        return
    if the_sum == n and the_prod == n:
        ps_sizes.add(len(ps_set))
        return
    if the_prod == n and n > the_sum: # product is correct, sum < n, so add a bunch of 1s
        ps_sizes.add(len(ps_set) + n-the_sum)
        return
    divisors = sorted(find_divisors(n//the_prod)[1:], reverse=True)
    if the_prod > 1:
        divisors.insert(0, n//the_prod)
    for div in divisors:
        if len(ps_set) > 0 and div > ps_set[-1]:
            continue
        new_set = ps_set.copy()
        new_set.append(div)
        find_ps_set_sizes(n, ps_sizes, new_set, the_sum+div, the_prod*div)


ps_minimums = [ 0 for _ in range(12001)]

# no set is possible for primes because only factors are 1 and self, so sum of factors is always greater than the number
primes_to_24k = set(prime_sieve(24001))

for x in range(2, 24001):
    if x in primes_to_24k:
        continue
    ps_sizes = set()
    find_ps_set_sizes(x, ps_sizes)
    for s in ps_sizes:
        if s > 12000:
            continue
        if ps_minimums[s] == 0:
            ps_minimums[s] = x
print(sum(set(ps_minimums)))



