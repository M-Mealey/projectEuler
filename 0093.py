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
import itertools
from itertools import combinations

def apply_ops(st, x):
    results = set()
    for s in st:
        results.add(s+x)
        results.add(s*x)
        results.add(s-x)
        results.add(x-s)
        if s !=0:
            results.add(x/s)
        if x != 0:
            results.add(s/x)
    return results

def get_possible_targets(t):
    possible_targets = set()
    list_perms = itertools.permutations(t)
    for p in list_perms:
        im_set = set()
        im_set.add(p[0])
        im_set_2 = apply_ops(im_set, p[1])
        im_set_3 = apply_ops(im_set_2, p[2])
        im_set_4 = apply_ops(im_set_3, p[3])
        for i in im_set_4:
            if i>0 and abs(i - round(i)) < 0.00001:
                possible_targets.add(i)
        # 2 and 2
        im_set_a = set()
        im_set_a.add(p[0])
        im_set_a2 = apply_ops(im_set_a, p[1])
        im_set_b = set()
        im_set_b.add(p[2])
        im_set_b2 = apply_ops(im_set_b, p[3])
        im_set_2u = set()
        for b in im_set_b2:
            im_set_22 = apply_ops(im_set_a2, b)
            im_set_2u.update(im_set_22)
        for i in im_set_2u:
            if i>0 and abs(i - round(i)) < 0.00001:
                possible_targets.add(i)
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
longest_sequence = 0
best_combo = (0,0,0,0)
for c in combos:
    res = get_possible_targets(c)
    s_len = find_longest_sequence(res)
    if s_len > longest_sequence:
        longest_sequence = s_len
        best_combo = c
#print(f"best combo: {best_combo}")
#print(f"seq len: {longest_sequence}")
#res = get_possible_targets(best_combo)
#print(list(res))
print(f"{best_combo[0]}{best_combo[1]}{best_combo[2]}{best_combo[3]}")
