"""
Project Euler Problem 106
=========================

Let S(A) represent the sum of elements in set A of size n. We shall call
it a special sum set if for any two non-empty disjoint subsets, B and C,
the following properties are true:

 1. S(B) S(C); that is, sums of subsets cannot be equal.
 2. If B contains more elements than C then S(B) > S(C).

For this problem we shall assume that a given set contains n strictly
increasing elements and it already satisfies the second rule.

Surprisingly, out of the 25 possible subset pairs that can be obtained
from a set for which n = 4, only 1 of these pairs need to be tested for
equality (first rule). Similarly, when n = 7, only 70 out of the 966
subset pairs need to be tested.

For n = 12, how many of the 261625 subset pairs that can be obtained need
to be tested for equality?

NOTE: This problem is related to problems 103 and 105.
"""
from itertools import combinations


def solve():
    """
    solve problem 106
    Since the problem specifies that condition 2 is always satisfied, we only need to check
    the sums for equal sized subsets. To do this, use a list of numbers 1 to 12 to represent
    the position of an item in the original sorted set of 12.
    Iterate over the possible subset sizes (2-6)
    For each subset size, iterate over all possible subsets B. For symmetry/to avoid double
    counting, B will always be the subset with the smallest element. Then iterate over all
    possible C that can be made from the remaining elements.
    For each pair of subsets, B and C, represent as a sorted list and compare elements pairwise.
    The first element of B will always be smaller than the first element of C. If this is true
    for all the elements in the list, then there is no need to compare sums because each element in
    B can be paired with an element in C that is strictly larger, so S(C) must be greater than S(B).
    Otherwise, add one to the total of subsets whose sums need to be checked.
    """
    total = 0
    # indices represent index of number in original sorted set
    indices = range(1, 13)
    for i in range(2, 7):  # test pairs of sets, sizes 2 to 6
        for s_b in combinations(indices, i):
            # the first set is the one with the smallest element, avoid double counting
            diff = set(indices[indices.index(s_b[0]):]) - set(s_b)
            for s_c in combinations(sorted(diff), i):
                for b, c in zip(s_b, s_c):
                    if b > c:
                        total += 1
                        break
    return total


if __name__ == "__main__":
    print(solve())
