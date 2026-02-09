"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""
import math

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def find_nth_permutation(n, ls):
    ans_str = ""
    index = n - 1 # n is 1-indexed, so subtract 1
    while len(ls) > 0:
        ls.sort()
        num_perms_starting_with_each = math.perm(len(ls)-1, len(ls)-1)
        index_of_next = index // num_perms_starting_with_each
        ans_str += str(ls.pop(index_of_next))
        index = index % num_perms_starting_with_each
    return ans_str


def euler_problem_24():
    print(find_nth_permutation(1000000, digits))

if __name__ == "__main__":
    euler_problem_24()
