"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import time

MAX_N = 1000000


def dict_comp(n, d):
    """
    Recursively find the path length for the given number.
    Add any path lengths found along the way to the dict, too.
    """
    if n in d:
        return d[n]
    if n % 2 == 0:
        path_len = dict_comp(n//2, d) + 1
        d[n] = path_len
        return path_len
    path_len = dict_comp(3*n + 1, d) + 1
    d[n] = path_len
    return path_len


def solve():
    """ Solve problem 14 """
    seq_dict = {1: 1}

    for n in range(2, MAX_N):
        if n not in seq_dict:
            dict_comp(n, seq_dict)
    max_key = max(seq_dict, key=seq_dict.get)
    return max_key


def get_next_set(s):
    """
    Given a set of numbers, return a set of numbers that lead to numbers in that set
    """
    new_set = set()
    for n in s:
        if 2*n < MAX_N:
            new_set.add(2*n)
        if (n-1) % 3 == 0:
            new_set.add((n-1)//3)
    return new_set


def solve_tree():
    """
    Attempting to solve the problem faster by proactively filling out
    the path length for some of the shorter paths
    It is a little slower than the dictionary solve method :(
    """
    numbers_found = {}
    this_set = set()
    this_set.add(1)
    p_len = 2

    while this_set:
        new_set = get_next_set(this_set)
        this_set = set(x for x in new_set if x not in numbers_found)
        numbers_found.update(dict.fromkeys(new_set, p_len))
        p_len += 1

    for n in range(2, MAX_N):
        if n not in numbers_found:
            dict_comp(n, numbers_found)

    max_key = max(numbers_found, key=numbers_found.get)
    return max_key


if __name__ == "__main__":
    start_time = time.perf_counter()
    print(solve())
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    # print(f"time: {elapsed_time}")
