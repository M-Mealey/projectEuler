"""
Project Euler Problem 66
========================

Consider quadratic Diophantine equations of the form:

                              x^2 - Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 =
1.

It can be assumed that there are no solutions in positive integers when D
is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
9^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D 7, the largest x is
obtained when D=5.

Find the value of D 1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
import sys
import os
from math import sqrt, floor


sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from eul_0065 import calculate_convergent   # pylint: disable=C0413
from eul_0064 import get_a_values   # pylint: disable=C0413

def get_convergent_list(a_v):
    """
    get list of convergent values
    """
    convergents = []
    if len(a_v) % 2 == 0:
        a_v = a_v + a_v[1:-1]
    for i in range(len(a_v)):
        ls = a_v[:i+1]
        convergents.append(calculate_convergent(ls))
    return convergents


def solve():
    """ solve problem 66 """
    max_x, d_index = 9, 5
    for d in range(2, 1000):
        if sqrt(d) == floor(sqrt(d)):
            continue  # problem assumes no solutions for square D
        a_vals = get_a_values(d)
        c_list = get_convergent_list(a_vals)
        for x, y in c_list:
            if x ** 2 - d * (y ** 2) == 1 and x > max_x:
                max_x = x
                d_index = d
    return d_index


if __name__ == "__main__":
    print(solve())
