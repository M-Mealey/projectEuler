"""
Project Euler Problem 16
========================

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def euler_problem_16():
    # The naive way to do this is to calculate 2^1000 and iterate over its digits, adding them together
    x = 2 ** 1000
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    print(sum)

if __name__ == "__main__":
    euler_problem_16()