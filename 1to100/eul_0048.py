"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def euler_problem_48():
    print(sum([x**x for x in range(1, 1001)]) % 10000000000)


if __name__ == "__main__":
    euler_problem_48()
