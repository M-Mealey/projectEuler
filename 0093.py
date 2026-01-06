"""
Project Euler Problem 93
========================

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
making use of the four arithmetic operations (+, , *, /) and
brackets/parentheses, it is possible to form different positive integer
targets.

For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.

Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
target numbers of which 36 is the maximum, and each of the numbers 1 to 28
can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest
set of consecutive positive integers, 1 to n, can be obtained, giving your
answer as a string: abcd.
"""
from itertools import combinations

def get_possible_targets(t):
    a, b, c, d = t[0], t[1], t[2], t[3]
    possible_targets = set()
    # find all the solutions :)
    # all of the operations can be thought of as pairwise, so start with 2 from set, apply all operations b/t
    # them to get intermediate set, then apply operations between each in intermediate set and 3rd number to get
    # another intermediate set, then 4th number, then switch 3rd and 4th number
    # repeat for every initial 2 numbers
    return possible_targets

def find_longest_sequence(s):
    n = 1
    while n in s:
        n += 1
    return n-1

combos = combinations(range(10), 4)


