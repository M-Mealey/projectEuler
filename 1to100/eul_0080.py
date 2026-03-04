"""
Project Euler Problem 80
========================

It is well known that if the square root of a natural number is not an
integer, then it is irrational. The decimal expansion of such square roots
is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum
of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital
sums of the first one hundred decimal digits for all the irrational square
roots.
"""
from decimal import *
import math

# set decimal precision to 102 places to avoid rounding
getcontext().prec = 102

digit_sum = 0
for x in range(1, 101):
    if math.floor(math.sqrt(x)) == math.sqrt(x):
        continue # skip squares
    s = Decimal(x).sqrt()
    decimal_digits = str(s).replace(".","")[:100]
    digit_sum += sum([int(x) for x in decimal_digits])

def euler_problem_80():
    print(digit_sum)

if __name__ == "__main__":
    euler_problem_80()
