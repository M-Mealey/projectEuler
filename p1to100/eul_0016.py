"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solve():
    # The naive way to do this is to calculate 2^1000 and iterate over its digits, adding them together
    x = 2 ** 1000
    total = 0
    while x > 0:
        total += x % 10
        x = x // 10
    return total


if __name__ == "__main__":
    print(solve())
