"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""
from local_helpers import is_prime

twice_squares = [2*x*x for x in range(1, 1000)]


def euler_problem_46():
    for i in range(3, 10001, 2):
        if not is_prime(i):
            sum_found = False
            for s in twice_squares:
                if s > i:
                    break
                if is_prime(i - s):
                    sum_found = True
            if not sum_found:
                print(i)
                break


if __name__ == "__main__":
    euler_problem_46()
