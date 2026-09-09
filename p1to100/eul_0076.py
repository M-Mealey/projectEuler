"""
Project Euler Problem 76
========================

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least
two positive integers?
"""
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from eul_0031 import find_combinations_dynamic as find_combinations   # pylint: disable=C0413


def solve():
    """ solve problem 76 """
    # copied coin solving logic from problem 31, but it's inefficient
    p_amounts = list(range(1, 100))
    return find_combinations(p_amounts, 100)


if __name__ == "__main__":
    print(solve())
