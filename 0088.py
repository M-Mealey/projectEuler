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
from helpers import find_divisors
import math


# for integer n, finds the unique lengths of all ps sets that can be made for that number
# writes the values to ps_sizes
# @TODO: make this more efficient. maybe look at factors from largest to smallest, and compute when adding a bunch of 1s
#  will complete the list without needing to do the recursion
def find_ps_set_sizes(n, ps_sizes, ps_set=[]):
    if sum(ps_set) > n or math.prod(ps_set) > n:
        return None
    if sum(ps_set) == n and math.prod(ps_set) == n:
        print(f"SET FOR {n}: {ps_set}")
        ps_sizes.add(len(ps_set))
    divisors = find_divisors(n)
    for div in divisors:
        if len(ps_set) > 0 and div < ps_set[-1]:
            continue
        new_set = ps_set.copy()
        new_set.append(div)
        find_ps_set_sizes(n, ps_sizes, new_set)


ps_minimums = [ 0 for _ in range(12001)]
ps_minimums[2] = 4
ps_minimums[3] = 6

ps_sizes = set()
find_ps_set_sizes(5, ps_sizes)
print(list(ps_sizes))

for x in range(2, 24001):
    ps_sizes = set()
    print(x)
    find_ps_set_sizes(x, ps_sizes)
    for s in ps_sizes:
        if ps_minimums[s] == 0:
            ps_minimums[s] = x
print(sum(ps_minimums))

