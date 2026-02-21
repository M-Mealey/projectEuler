"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""
import math
from local_helpers import is_prime


def find_prime(x):
    i = 0
    num = 1
    while i < x:
        i += 1
        num += 1
        while not is_prime(num):
            num += 1
    return num


def euler_problem_7():
    print(find_prime(10001))


if __name__ == "__main__":
    euler_problem_7()
