"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""
import math
from math import factorial
import time

"""
Computes nCr for given n and r
"""


def ncr(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))


"""
Each step is either in the +x or +y direction, 
so for a 20x20 grid every path will consist of exactly 40 steps
The total number of paths is therefore the number of ways you can arrange the 20 +x steps
within the list of 40 total steps (with the rest of the steps being +y)
It's equivalent to figuring out how many ways you can flip a coin 40 times and end up with
20 heads and 20 tails
Mathematically, this can be calculated as nCr, where n=40 and r=20
"""


def euler_problem_15(compare=False):
    start_time = time.perf_counter()
    print(math.comb(40, 20))
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    if compare:
        print(f"solve with math lib took {elapsed_time} seconds")

        start_time = time.perf_counter()
        print(ncr(40, 20))
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"solve with written method took {elapsed_time} seconds")


if __name__ == "__main__":
    compare_solutions = True
    euler_problem_15(compare_solutions)
