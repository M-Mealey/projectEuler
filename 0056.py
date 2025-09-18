"""
Project Euler Problem 56
========================

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is
the maximum digital sum?
"""

def get_digit_sum(x):
    digit_sum = 0
    while x>0:
        digit_sum += x%10
        x = x//10
    return digit_sum

max_digit_sum = 0
for a in range(1,100):
    for b in range(1,100):
        max_digit_sum = max(max_digit_sum, get_digit_sum(a**b))
print(max_digit_sum)


