"""
Project Euler Problem 95
========================

The proper divisors of a number are all the divisors excluding the number
itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of
the proper divisors of 284 is 220, forming a chain of two numbers. For
this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with
12496, we form an amicable chain of five numbers:

                12496 14288 15472 14536 14264 ( 12496 ...)

Find the smallest member of the longest amicable chain with no element
exceeding one million.
"""
from helpers import find_divisors

# from problem 21
amicable_numbers = []
for i in range(1000000):
    divisor_sum = sum(find_divisors(i))
    if divisor_sum != i and sum(find_divisors(divisor_sum)) == i:
        amicable_numbers.append(i)

print(sum(amicable_numbers))

# probably better to make array of 1M elements, iterate 1 to 1M, for each number add it to the element at
# each of its multiples' indexes
# start with array of 1s: (all will have 1 as a divisor except 0 and 1]
# [0, 0, 1, 1, 1, 1, 1, 1, 1, 1 ...]
# next number is 2
# [0, 1, 1, 1, 3, 1, 3, 1, 3, 1, ...]
# 3
# [0, 1, 1, 1, 2, 1, 5, 1, 2, 4 ...]
# then find loops using Floyd's cycle detection algorithm: https://en.wikipedia.org/wiki/Cycle_detection
#

