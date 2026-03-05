"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def arith_sum(a, x):
    """Computes sum of arithmetic series from 0 to a, interval of x"""
    n = a // x
    total = x * n * (n + 1) / 2
    return int(total)


def sum_3_5(x):
    """Returns sum of all natural numbers below x that are multiples of 3 or 5"""
    total = arith_sum(x - 1, 3) + arith_sum(x - 1, 5) - arith_sum(x - 1, 15)
    return int(total)


def euler_problem_1():
    print(sum_3_5(1000))


if __name__ == "__main__":
    euler_problem_1()
