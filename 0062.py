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

sorted_cubes = {}
smallest_cube = {}

for x in range(10, 10000):
    c = x**3
    # rearrange the digits in descending order. This forms a fingerprint that is the same for all permutations
    digits_sorted = int("".join(sorted([ch for ch in str(c)], reverse=True)))
    matches = sorted_cubes.get(digits_sorted, 0)
    if matches == 0: # if there are no matching entries, this is the smallest cube with these digits.
        smallest_cube[digits_sorted] = c
    if matches == 4: # if this is the 5th match, search is over, return smallest cube for these digits
        print(smallest_cube[digits_sorted])
        break
    sorted_cubes[digits_sorted] = matches + 1

