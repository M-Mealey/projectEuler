"""
Project Euler Problem 62
========================

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also
cube.

Find the smallest cube for which exactly five permutations of its digits
are cube.
"""
import itertools

cubes = [x**3 for x in range(300, 10000)]

def to_int(tup):
    total = 0
    for t in tup:
        total *= 10
        total += t
    return total

for c in cubes:
    permutation_lists = list(itertools.permutations([int(ch) for ch in str(c)]))
    permutations = set([to_int(p) for p in permutation_lists])
    cube_permutations = [p for p in permutations if c <= p and p in cubes]
    if len(cube_permutations) == 5:
        print(c)
        break

