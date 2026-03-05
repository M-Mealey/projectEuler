"""
Project Euler Problem 71
========================

Consider the fraction, n/d, where n and d are positive integers. If n < d
and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d 8 in ascending order
of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
                       5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d 1,000,000 in
ascending order of size, find the numerator of the fraction immediately to
the left of 3/7.
"""
# @TODO: check if fractions are reduced?

# immediately to left = closest to 3/7 without going over
# for denominator d, solve x = (3/7)*d to get numerator that makes fraction equal to 3/7
# if numerator is not integer (most cases), round down
# if numerator is an integer (happens when d is multiple of 7), subtract 1
# do this for each possible denominator

import math

closest_fraction = (2, 5)
for d in range(7, 1000001):
    x = (3/7) * d
    if math.floor(x) == x:
        x = x-1
    else:
        x = math.floor(x)
    if (3/7) - (closest_fraction[0]/closest_fraction[1]) > (3/7) - (x/d):
        closest_fraction = (x, d)


def euler_problem_71():
    print(closest_fraction[0])


if __name__ == "__main__":
    euler_problem_71()
