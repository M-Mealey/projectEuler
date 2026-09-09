"""
Project Euler Problem 67
========================

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

                                    3
                                   7 4
                                  2 4 6
                                 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not
possible to try every route to solve this problem, as there are 2^99
altogether! If you could check one trillion (10^12) routes every second it
would take over twenty billion years to check them all. There is an
efficient algorithm to solve it. ;o)
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from eul_0018 import find_max_path_sum   # pylint: disable=C0413


def solve(input_files=("resources/triangle.txt",)):
    """ solve problem 67 """
    with open(input_files[0], 'r', encoding='utf-8') as f:
        pyramid_input = f.read()

    # all below is copied from problem 16

    # convert string to array of ints
    pyramid = [[int(x) for x in row.strip().split()]
               for row in pyramid_input.strip().splitlines()]

    return find_max_path_sum(pyramid)


if __name__ == "__main__":
    print(solve())
