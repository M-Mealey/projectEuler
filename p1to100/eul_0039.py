"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""
import math


def solve():
    """ solve problem 39 """
    # generate squares to save time checking later
    squares = set([x ** 2 for x in range(1, 1000)])
    # solutions dict, key is perimeter, value is list of tuples (a,b,c) that form right triangle with perimeter p
    solutions = {}
    for a in range(2, 999):
        # c > a, so 1000-2a is a soft upper limit on b. Is there a better limit?
        for b in range(2, 1000-2*a):
            c_sq = a**2 + b**2
            if c_sq in squares:
                c = int(math.sqrt(c_sq))
                p = a+b+c
                if p in solutions:
                    solutions[p].append((a, b, c))
                else:
                    solutions[p] = [(a, b, c)]
    answer = max(solutions, key=lambda k: len(solutions[k]))
    return answer


if __name__ == "__main__":
    print(solve())
