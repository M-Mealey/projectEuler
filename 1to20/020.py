"""
Project Euler Problem 20
========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

import math

f100 = math.factorial(100)

digit_sum = 0
while f100 > 0:
    digit_sum += f100%10
    f100 = f100//10

print(digit_sum)

